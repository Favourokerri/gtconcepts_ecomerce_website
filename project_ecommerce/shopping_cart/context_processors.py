from shopping_cart.models import CartItem

def cart_items_count(request):
    cart_items = CartItem.objects.all()
    number_of_items = sum(cart_item.quantity for cart_item in cart_items)
    return {'number_of_items': number_of_items}