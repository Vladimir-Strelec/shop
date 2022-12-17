from django.urls import path

from shop.account.views import UserShopView, RegisterUser, UserLoginView

urlpatterns = (
    path('', UserShopView.as_view(), name='users'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
)
