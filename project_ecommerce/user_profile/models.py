from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ShippingFee(models.Model):
    location = models.CharField(max_length=300, unique=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.location

class Profile(models.Model):
    """ 
        models for users. 
        using relationship to extend the user field
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    martriculation_number = models.CharField(max_length=200, null=True, blank=True, default="for student loan only")
    location = models.ForeignKey(ShippingFee, on_delete=models.CASCADE, blank=True, null=True)
    Home_address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username