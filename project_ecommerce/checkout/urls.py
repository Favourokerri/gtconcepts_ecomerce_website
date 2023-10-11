from django.urls import path
from .views import checkout, shipping_details

urlpatterns = [
    path('checkout/', checkout, name="checkout"),
    path('details/', shipping_details, name="shipping_details"),
  
]
