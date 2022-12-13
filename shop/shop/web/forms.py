from django import forms

from shop.account.models import UserShop
from shop.web.models import Product, Category


class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'image', 'description', 'price', 'new_price', 'manufacturer', 'promotion', 'category', 'url']
