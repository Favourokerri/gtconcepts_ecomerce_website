from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Cart, Order, OrderItem
from user_profile.models import Profile, ShippingFee
from django.contrib import messages
from .mails import send_mail_after_order
from .mails import send_mail_after_order_to_admin
from company_details.models import Account_detail
import uuid

def shipping_details(request):
    shippingFees = ShippingFee.objects.all()
    context = {"shippingFees": shippingFees}

    if request.method == "POST":
        user_profile = Profile.objects.get(user=request.user)
        if not user_profile.phone_number:
            messages.warning(request, "Please fill in your phone number")
            return redirect('profile')

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

    return render(request, 'checkout/shipping_details.html', context)

def checkout(request):
    """ view for checkout"""
    user_profile = Profile.objects.get(user=request.user)
    cart = Cart.objects.get(user=request.user, completed=False)
    admin_bank_account = Account_detail.objects.filter(is_active=True).first()
    selected_location = user_profile.location
    address = user_profile.Home_address
    number = user_profile.phone_number
    shipping_fee = ShippingFee.objects.get(location=selected_location)
    total_price = sum(item.total_price() for item in cart.cartitems.all())
    total_price_with_shipping_fee = total_price + shipping_fee.fee

    # Check if the 'description' (for transfer) is already stored in the session
    # this block is to ensure that description stays consistent in the checkout view and admin site
    if 'description' in request.session:
        description = request.session['description']
    else:
        # If not, generate a new random 'description' and store it in the session
        description = Order.generate_random_string()
        request.session['description'] = description

    
    if request.method == "POST":
        """ Placing order"""
        orders = Order.objects.create(user=request.user,
                                      shipping_fee=shipping_fee.fee,
                                      address=address,
                                      phone_number=number,
                                      total_price=total_price_with_shipping_fee,
                                      description=description)
        
        #delete session in order to create a new random string
        del request.session['description']
        request.session.save()
        
        # Create OrderItem instances for each item in the cart and associate them with the order
        order_items = [] # for sending of mails
        for cart_item in cart.cartitems.all():
            order_item = OrderItem.objects.create(
                order=orders,
                product=cart_item.product,
                quantity=cart_item.quantity,
                total_price=cart_item.total_price(),
            )
            order_items.append(order_item)
        
        # Set the order_items field in the Order model to the list of order_item instances
        orders.order_items.set(order_items)

        cart.completed = True
        cart.save()
        messages.success(request, "your order has been placed successfully")
        send_mail_after_order(request, request.user, order_items)
        send_mail_after_order_to_admin(request, request.user, orders, order_items)
        return redirect('profile')
    
    context = {
        "total_price": total_price,
        "shipping_fee": shipping_fee,
        "total_price_with_shipping_fee": total_price_with_shipping_fee,
        "description": description,
        "admin_bank_account": admin_bank_account,
    }
    return render(request, 'checkout/checkout.html', context)