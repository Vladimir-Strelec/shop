from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from shop.web.forms import RegisterUserForm
from shop.web.models import UserShop


class UserShopView(generic.ListView):
    model = UserShop
    queryset = UserShop.objects.all()
    template_name = "User.html"


class RegisterUser(generic.CreateView):
    model = UserShop
    form_class = RegisterUserForm
    template_name = "register_user.html"
    success_url = reverse_lazy('users')
