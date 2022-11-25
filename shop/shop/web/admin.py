from django.contrib import admin
from django.contrib.auth.models import User

from shop.web.models import UserShop

admin.site.register(UserShop)
