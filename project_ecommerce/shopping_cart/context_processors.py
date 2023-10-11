from shopping_cart.models import CartItem
from shopping_cart.models import Cart
from django.contrib.auth.models import User

def cart_items_count(request):
    """ getting the number of items in cart"""
    if request.user.is_authenticated:
        try:
            user_cart = Cart.objects.get(user=request.user, completed=False)  # Retrieve the user's cart
            cart_items = CartItem.objects.filter(cart=user_cart)  # Filter cart items by the user's cart
            number_of_items = sum(cart_item.quantity for cart_item in cart_items)
            return {'number_of_items': number_of_items}
        except Cart.DoesNotExist:
            number_of_items = 0
            return {'number_of_items': number_of_items}
    else:
        cart_items = []
        number_of_items = 0
        return {'number_of_items': number_of_items}