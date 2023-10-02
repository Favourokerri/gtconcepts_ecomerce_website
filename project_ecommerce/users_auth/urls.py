from django.contrib import admin
from django.urls import path
from users_auth import views

urlpatterns = [
    path('signup', views.sing_up, name="signup"),
    path('login', views.log_in, name='login'),
]