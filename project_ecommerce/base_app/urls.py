from django.contrib import admin
from django.urls import path
from base_app import views

urlpatterns = [
    path('', views.index, name="index"),
]