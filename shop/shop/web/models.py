from django.core.validators import MinLengthValidator
from django.db import models

from shop.account.models import UserShop
from shop.validators.custom_validators import validate_only_letters


class Category(models.Model):
    title = models.CharField("Title", max_length=100)
    url = models.SlugField(max_length=160, unique=True)
    is_active_in_filter = models.BooleanField("Is activ in filters", default=False)
    is_active_in_bank = models.BooleanField("Is activ in bank", default=False)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    name = models.CharField("Name", max_length=100)
    image = models.ImageField("Image", upload_to='images/%Y-%m-%d/')
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    new_price = models.DecimalField("New price", max_digits=5, decimal_places=2, blank=True, null=True)
    manufacturer = models.CharField("Manufacturer", max_length=160, validators=(MinLengthValidator(2),
                                                                                validate_only_letters))
    promotion = models.BooleanField("Promotion", default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserShop, on_delete=models.CASCADE, blank=True, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return f"{self.name} - {self.price}$ - {self.category}"
