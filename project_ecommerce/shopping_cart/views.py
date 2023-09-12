from django.shortcuts import render
from django.http import JsonResponse
import json
from store.models import Product
from shopping_cart.models import Cart, CartItem
# Create your views here.
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        print(cartitem)


    return JsonResponse("item added to cart successfully", safe=False)