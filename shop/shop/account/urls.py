from django.urls import path
from django.views.generic import TemplateView

from shop.account.views import RegisterUser, UserLoginView, VerifyEmailView

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register'),

    path('login/', UserLoginView.as_view(), name='login'),

    path('confirm/email/', VerifyEmailView.as_view(), name='verify_email'),
    path('verify/email/<uidb64>/<token>/', TemplateView.as_view(template_name='confirm_email.html'),
         name='confirm_email'),
)
