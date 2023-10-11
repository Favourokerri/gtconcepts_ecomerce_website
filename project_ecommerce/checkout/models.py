from django.db import models
from shopping_cart.models import Cart, CartItem
from django.contrib.auth.models import User
from store.models import Product
import uuid

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)  # Reference to the order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for this item

    DELIVERY_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('RETURNED', 'Returned'),
    )

    delivery_status = models.CharField(
        max_length=10,
        choices=DELIVERY_STATUS_CHOICES,
        default='PENDING',  # Set the default delivery status
    )

    def __str__(self):
        return f"OrderItem #{self.id} - {self.product.name} ({self.quantity} units)"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_items = models.ManyToManyField(OrderItem, related_name='orders')
    
    PAYMENT_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded'),
    )

    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='PENDING',  # Set the default payment status
    )

    DELIVERY_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('RETURNED', 'Returned'),
    )

    delivery_status = models.CharField(
        max_length=10,
        choices=DELIVERY_STATUS_CHOICES,
        default='PENDING',  # Set the default delivery status
    )

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"