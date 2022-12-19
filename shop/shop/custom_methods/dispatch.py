from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from shop.account.models import UserShop


class CheckLogin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            UserShop.objects.get(slug=request.session['user_slug'])
            return HttpResponseRedirect('')
        except:
            return HttpResponseRedirect('account/login/')




