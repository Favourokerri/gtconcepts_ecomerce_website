from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib import messages
from store.models import Product
from shopping_cart.models import Cart, CartItem
# Create your views here.
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    number_of_items = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        messages.success(request, "Item added to cart successfully")

    return JsonResponse("item added successfully", safe=False)

def update_item(request):
    data = json.loads(request.body)
    product_id = data["id"]
    action = data['action']
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if action == 'decrease':
            if cartitem.quantity < 2:
                cartitem.delete()
            else:
                cartitem.quantity -= 1
                cartitem.save()
        elif action == 'increase':
            cartitem.quantity += 1
            cartitem.save()
        elif action == 'remove':
            cartitem.delete()
       
    return JsonResponse("item updated successfully", safe=False)


def cart(request):
    """View for our cart page"""
    cart_items = CartItem.objects.all()
    cart_total = sum(cart_item.total_price() for cart_item in cart_items)
    
    context = {
        "cart_items": cart_items,
        "cart_total": cart_total,
    }

    #note getting number of cartitems is in the context_processor file
    return render(request, "cart.html", context)