from django.contrib import admin
from django.urls import path
from user_profile import views

urlpatterns = [
    path('user', views.profile, name="profile"),
    path('edith_profile', views.edith_profile, name="edith_profile"),
]