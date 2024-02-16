from django.urls import path
from .views import index, product_list, product_detail, order_create, order_list, add_to_products

urlpatterns = [
    path('', index, name='index'),
    path('add_to_products/', add_to_products, name='add_to_products'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/<int:product_id>/order/', order_create, name='order_create'),
    path('orders/', order_list, name='order_list'),
]
