"""
URL configuration for project_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('base_app.urls')),
    path('products/', include('store.urls')),
    path('cart/', include('shopping_cart.urls')),
    path('blog/', include('blog_app.urls')),
    path('user/', include('users_auth.urls')),
    path('profile/', include('user_profile.urls')),
    path('checkout/', include('checkout.urls')),
    path('info/', include('company_details.urls')),
    path('query/', include('search.urls')),
]

urlpatterns += staticfiles_urlpatterns()
handler404 = 'base_app.views.custom_404_view'
handler505 = 'base_app.views.custom_500_view'