import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver

from shop.validators.custom_validators import validate_only_letters
User

class UserShop(models.Model):
    name = models.CharField("Name", max_length=150, validators=(MinLengthValidator(2), validate_only_letters), )
    password = models.CharField("Password", max_length=50)
    email = models.EmailField("Email", error_messages={
        "unique": _(f"A Email with that Emails already exists."),
    }, )
    telephone = models.IntegerField("Telephone number")
    address = models.CharField("Address", max_length=300)
    data_joined = models.DateTimeField("Data joined", default=timezone.now)
    slug = models.SlugField(max_length=160, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        return self.password

    def check_password(self, raw_password):

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def __str__(self):
        return f"{self.name} - {self.email}"


# @receiver(pre_save, sender=UserShop)
# def hashing(sender, instance, **kwargs):
#     instance.password = instance.set_password(instance.password)
