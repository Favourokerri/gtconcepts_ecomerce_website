from django.contrib import admin
from django.urls import path
from users_auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('token', views.token_send, name="token_send"),
    path('verify/<str:auth_token>/', views.verify_account, name='verify_account'),
    path('resend_verification', views.resend_verification, name="resend_verification"),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name="logout"),
    path('password-reset/', views.ResetPasswordView.as_view(), name='reset_password/password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/reset_confrim.html'),
         name='password_reset_complete'),
]