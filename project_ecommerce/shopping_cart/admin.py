from django.contrib import admin
from shopping_cart.models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'completed')
    list_filter = ('id', 'user', 'completed')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity')
    list_filter = ('product', 'cart')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
