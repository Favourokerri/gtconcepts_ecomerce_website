from django.contrib import admin
from django.urls import path
from shopping_cart import views

urlpatterns = [
    path('user', views.add_to_cart, name="user"),
]