from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from shop.custom_methods.dispatch import CheckLogin
from shop.web.forms import CreateProductForm
from shop.web.models import Product


class ProductView(CheckLogin, generic.ListView):
    model = Product
    template_name = "base.html"


class CreateProductView(generic.CreateView, LoginRequiredMixin):
    model = Product
    queryset = Product.objects.all()
    form_class = CreateProductForm
    success_url = reverse_lazy('create_product')
