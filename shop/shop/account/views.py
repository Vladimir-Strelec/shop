

from django.contrib import auth
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import capfirst

from django.urls import reverse_lazy, reverse
from django.utils.functional import lazy
from django.views import generic

from shop.account.forms import RegisterUserForm, LoginForm
from shop.account.models import UserShop


class UserShopView(generic.ListView):
    model = UserShop
    queryset = UserShop.objects.all()
    template_name = "User.html"


class RegisterUser(generic.CreateView):
    model = UserShop
    form_class = RegisterUserForm
    template_name = "register_user.html"
    success_url = reverse_lazy('users')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.form_valid(form)
            return self.success_url
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))



class UserLoginView(views.FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('create_product')
    form_class = LoginForm

    def form_valid(self, form):
        user = UserShop(name=form.cleaned_data['name'])
        password = form.cleaned_data['password']
        x = user.check_password(password)

        return HttpResponse('Net usera')

    def user_shop_add_in_session(self, user):
        self.request.session['user_slug'] = user.slug
        return self.success_url
