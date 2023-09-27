from django.db import models
import uuid
from django.contrib.auth.models import User
from store.models import Product
from django.utils import timezone

# Create your models here.
class Cart(models.Model):
    """ models for our cart"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
class CartItem(models.Model):
    """ models for our cartitems """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)  # Set a default value
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
      """ to calculate total price of each product """
      total = self.product.price * self.quantity
      return total
   
    def __str__(self):
        return self.product.name