from django.contrib.auth import authenticate, get_user_model
from django.forms.models import ModelForm
from django import forms
from shop.account.models import UserShop


class RegisterUserForm(forms.models.ModelForm):
    class Meta:
        model = UserShop
        fields = '__all__'

    def save(self, *args, **kwargs):
        user = UserShop.objects.create(**self.cleaned_data)
        user.password = user.set_password(user.password)
        user.save()


class LoginForm(forms.Form):
    name = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50)

