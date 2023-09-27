from django.contrib import admin
from django.urls import path
from shopping_cart import views

urlpatterns = [
    path('add_to_cart', views.add_to_cart, name="add"),
    path('cart', views.cart, name="cart"),
    path('update', views.update_item, name="update_item")
]