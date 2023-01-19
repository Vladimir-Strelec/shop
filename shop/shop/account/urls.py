from django.urls import path
from django.views.generic import TemplateView

from shop.account.views import RegisterUser, UserLoginView, VerifyEmailView

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register'),
    path('', UserLoginView.as_view(), name='login'),
    path('confirm_email/', TemplateView.as_view(template_name='email-verify/confirm_email.html'), name='confirm_amail'),

    path('verify_email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
)
