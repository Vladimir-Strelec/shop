from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from shop.account.models import UserShop

admin.site.register(UserShop)
