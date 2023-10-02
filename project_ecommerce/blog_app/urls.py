from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('blogs', views.blog, name="blog"),
]
