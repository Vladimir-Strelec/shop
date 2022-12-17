from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from shop.web.forms import CreateProductForm, CreateProductForm
from shop.web.models import Product

User

class ProductView(generic.ListView):
    model = Product
    template_name = "index.html"


class CreateProductView(generic.CreateView, LoginRequiredMixin):
    model = Product
    queryset = Product.objects.all()
    form_class = CreateProductForm
    success_url = reverse_lazy('create_product')



    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     if form.is_valid():
    #         form.save()

