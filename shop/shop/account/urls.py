from django.urls import path

from shop.account.views import RegisterUser, UserLoginView

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
)
