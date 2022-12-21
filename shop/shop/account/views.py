
from django.contrib import auth
from django.contrib.auth import views, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import capfirst

from django.urls import reverse_lazy, reverse
from django.utils.functional import lazy
from django.views import generic, View
from django.views.generic import CreateView

from shop.account.forms import RegisterUserForm, LoginForm
from shop.account.models import UserShop





class UserLoginView(views.FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('products')
    form_class = LoginForm

    def form_valid(self, form):
        current_user = get_object_or_404(UserShop, email=form.cleaned_data['email'])
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')

        if current_user.check_password(password) and password == password2:
            self.user_shop_add_in_session(current_user)
            return redirect(reverse_lazy('products'))

        self.success_url = reverse_lazy('login')
        return super(UserLoginView, self).form_valid(form)

    def user_shop_add_in_session(self, user):
        self.request.session['user_slug'] = user.slug


class RegisterUser(CreateView, UserLoginView):
    model = UserShop
    form_class = RegisterUserForm
    template_name = "register_user.html"
    success_url = reverse_lazy('products')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            self.form_valid(form)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': self.form_class})