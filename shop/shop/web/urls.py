from django.urls import path

from shop.web.views import UserShopView, RegisterUser

urlpatterns = (
    path('', UserShopView.as_view(), name='users'),
    path('register/', RegisterUser.as_view(), name='register'),
)
