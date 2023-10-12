from django.contrib import admin
from checkout.models import Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_status', 'delivery_status', 'phone_number', 'address']
    list_filter=['delivery_status', 'payment_status', 'order_date',]
    ordering = ['user']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'total_price', 'delivery_status', 'phone_number', 'order_address']
    list_filter=['delivery_status',]
    ordering =['order__user']

    def order_address(self, obj):
        return obj.order.address if obj.order.address else "not specified"
    
    def phone_number(self, obj):
        return obj.order.phone_number if obj.order.phone_number else "not specified"

   

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)