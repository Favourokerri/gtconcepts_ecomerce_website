from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Cart, Order, OrderItem
from user_profile.models import Profile, ShippingFee

def shipping_details(request):
    shippingFees = ShippingFee.objects.all()
    context = {"shippingFees": shippingFees}

    if request.method == "POST":
        user_profile = Profile.objects.get(user=request.user)
        city_name = request.POST['city']

        try:
            shipping_location = ShippingFee.objects.get(location=city_name)
            user_profile.location = shipping_location
            user_profile.Home_address = request.POST['street_address']
            user_profile.save()  # Save the updated user profile
            return redirect('checkout')
        except ShippingFee.DoesNotExist:
            user_profile.location = None
            user_profile.Home_address = request.POST['street_address']
            user_profile.save()  # Save the updated user profile

    return render(request, 'shipping_details.html', context)

def checkout(request):
    if request.method == "POST":
        user = request.user
        cart = Cart.objects.get(user=user, completed=False)

        # Calculate the total price of the items in the cart
        total_price = sum(item.total_price() for item in cart.cartitems.all())

        # Retrieve the user's profile to get the selected location
        user_profile = Profile.objects.get(user=user)
        selected_location = user_profile.location  # Assuming location is the foreign key to ShippingFee

        # Fetch the corresponding ShippingFee based on the selected location
        shipping_fee = ShippingFee.objects.get(location=selected_location)

        # Calculate the total price with shipping fee
        total_price_with_shipping_fee = total_price + shipping_fee.fee

        # Create a new Order
        order = Order.objects.create(user=user, total_price=total_price_with_shipping_fee)

        # Create OrderItem instances for each item in the cart and associate them with the order
        for cart_item in cart.cartitems.all():
            order_item = OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                total_price=cart_item.total_price(),
            )

        # Mark the Cart as completed
        cart.completed = True
        cart.save()

    return render(request, 'checkout.html')