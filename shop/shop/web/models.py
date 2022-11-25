from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver

from shop.web.custom_validators import validate_only_letters


class UserShop(models.Model):
    name = models.CharField("Name", max_length=150, validators=(MinLengthValidator(2), validate_only_letters), )
    password = models.CharField("Password", max_length=50)
    email = models.EmailField("Email", error_messages={
        "unique": _(f"A Email with that Emails already exists."),
    }, )
    telephone = models.IntegerField("Telephone number")
    address = models.CharField("Address", max_length=300)
    is_staff = models.BooleanField("staff status", default=False, )
    is_active = models.BooleanField("active", default=True, )
    data_joined = models.DateTimeField("Data joined", default=timezone.now)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        return self.password

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.name} - {self.email}"


@receiver(pre_save, sender=UserShop)
def hashing(sender, instance, **kwargs):
    instance.password = instance.set_password(instance.password)
