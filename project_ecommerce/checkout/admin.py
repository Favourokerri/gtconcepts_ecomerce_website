from django.contrib import admin
from checkout.models import Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'payment_status', 'delivery_status', 'order_date',]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'total_price', 'delivery_status',]
    list_filter=['product', 'delivery_status']

   

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)