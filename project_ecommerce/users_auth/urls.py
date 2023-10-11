from django.contrib import admin
from django.urls import path
from users_auth import views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('token', views.token_send, name="token_send"),
    path('verify/<str:auth_token>/', views.verify_account, name='verify_account'),
    path('resend_verification', views.resend_verification, name="resend_verification"),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name="logout"),
]