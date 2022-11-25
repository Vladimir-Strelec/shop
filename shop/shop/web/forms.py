from django.forms.models import ModelForm
from django.views.generic.edit import ModelFormMixin

from shop.web.models import UserShop


class RegisterUserForm(ModelForm):
    class Meta:
        model = UserShop
        fields = '__all__'
