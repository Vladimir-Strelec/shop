from django.urls import path

from shop.web.views import ProductView, CreateProductView

urlpatterns = (
    path("products/", ProductView.as_view(), name="products"),
    path("create/product/", CreateProductView.as_view(), name="create_product"),
)
