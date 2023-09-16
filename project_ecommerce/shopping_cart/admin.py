from django.contrib import admin
from shopping_cart.models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'completed')
    list_filter = ('id', 'user', 'completed')
    search_fields = ('id', 'user__username')

    def user_name(self, obj):
        return obj.cart.user.username

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'user_name', 'updated_at')
    list_filter = ('updated_at', 'cart__user__username')  # Add a filter by user's name
    search_fields = ('cart__user__username',)  # Enable searching by user's name

    def user_name(self, obj):
        return obj.cart.user.username

    user_name.short_description = 'User Name'  # Set a column header name for the user's name


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
