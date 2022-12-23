from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from django import forms
from shop.account.models import UserShop
UserCreationForm


class RegisterUserForm(forms.models.ModelForm, forms.Form):
    password = forms.CharField(max_length=50,)
    password2 = forms.CharField(max_length=50,)

    class Meta:
        model = UserShop
        fields = ('name', 'email', 'slug')

    def save(self, commit=False):
        user = UserShop.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            slug=self.cleaned_data['slug'])
        user.password = user.set_password(user.password)
        user.save()
        return self.instance

    # def save(self, commit=False):
    #     user = super().save(
    #         commit=False)
    #     user.password = user.set_password(user.password)
    #     user.save()
    #     if commit:
    #         user.save()
    #     return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

