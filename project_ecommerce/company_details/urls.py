from django.urls import path
from .views import contact_us, terms_and_conditions

urlpatterns = [
    path('contact_us/', contact_us, name="contact_us"),
    path('terms&conditions', terms_and_conditions, name="terms")
  
]
