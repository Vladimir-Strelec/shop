
from django.contrib import auth
from django.contrib.auth import views, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import capfirst

from django.urls import reverse_lazy, reverse
from django.utils.functional import lazy
from django.utils.http import urlsafe_base64_decode
from django.views import generic, View
from django.views.generic import CreateView

from shop.account.forms import RegisterUserForm, LoginForm
from shop.account.models import UserShop
from shop.account.utils import send_email_for_verify


class UserLoginView(views.FormView):
    template_name = 'login-logout/login.html'
    success_url = reverse_lazy('products')
    form_class = LoginForm

    def form_valid(self, form):
        current_user = get_object_or_404(UserShop, email=form.cleaned_data['email'])
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')

        if current_user.check_password(password) and password == password2:

            return send_email_for_verify(self.request, current_user)

        self.success_url = reverse_lazy('login')
        return super(UserLoginView, self).form_valid(form)


class RegisterUser(CreateView, UserLoginView):
    model = UserShop
    form_class = RegisterUserForm
    template_name = "account-register/register_user.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            self.form_valid(form)
            return redirect('confirm_amail')
        return render(request, self.template_name, {'form': self.form_class})


class VerifyEmailView(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user:
            self.user_shop_add_in_session(user)

        return render(request, 'index.html')

    def user_shop_add_in_session(self, user):
        self.request.session['user_slug'] = user.slug
        user.auth_user = True

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserShop.objects.get(id=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

