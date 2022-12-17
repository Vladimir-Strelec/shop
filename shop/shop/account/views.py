
from django.contrib import auth
from django.contrib.auth import views
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


class UserShopView(generic.ListView, LoginRequiredMixin):
    model = UserShop
    queryset = UserShop.objects.all()
    template_name = "User.html"

    def dispatch(self, request, *args, **kwargs):
        try:
            user = UserShop.objects.get(slug=self.request.session['user_slug'])
            if not user.is_authenticated:
                return super().dispatch(request, *args, **kwargs)
        except:
            return redirect(reverse_lazy('login'))





User
class RegisterUser(CreateView):
    model = UserShop
    form_class = RegisterUserForm
    template_name = "register_user.html"
    success_url = reverse_lazy('users')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        return HttpResponseRedirect(self.success_url)
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         x = form.save()
    #         return redirect('users', x)
    #     return super().post(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return reverse_lazy('users')
    #     return super(RegisterUser, self).post(self, request, args, kwargs)
    #
    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url.format(**self.object.__dict__)


class UserLoginView(views.FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('users')
    form_class = LoginForm

    def form_valid(self, form):
        current_user = get_object_or_404(UserShop, email=form.cleaned_data['email'])
        password = form.cleaned_data.get('password')

        if current_user.check_password(password):
            self.change_status_in_true_or_false(current_user)
            self.user_shop_add_in_session(current_user)
            return super(UserLoginView, self).form_valid(form)

        self.success_url = reverse_lazy('login')
        return super(UserLoginView, self).form_valid(form)

    def user_shop_add_in_session(self, user):
        self.request.session['user_slug'] = user.slug

    @staticmethod
    def change_status_in_true_or_false(current_user):
        current_user.is_authenticated = True
