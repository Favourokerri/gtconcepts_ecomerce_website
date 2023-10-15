from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from user_profile.models import Profile
from checkout.models import Order, OrderItem
from company_details.models import Contact_detail
from django.db import IntegrityError, OperationalError
import uuid

# Create your views here.
def profile(request):
    """ models for our profile"""
    contact_details = Contact_detail.objects.filter(is_major=True).first()
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user, auth_token=str(uuid.uuid4()))
        profile.save()

    orders = Order.objects.filter(user=request.user)
    order_items = OrderItem.objects.filter(order__user=request.user)
    context= {"profile":profile,
              "orders":orders,
              "order_items":order_items,
              "contact_details":contact_details,
              }

    return render(request, 'profile/profile.html', context)

def edith_profile(request):
    """ edith user profile"""
    if request.method=='POST':
        try:
            user = request.user
            profile = Profile.objects.get(user=request.user)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            profile.home_address = request.POST['address']
            profile.martriculation_number = request.POST['matriculation_number']
            profile.phone_number = request.POST[str('phone_number')]
            user.save()
            profile.save()
            messages.success(request, "profile edithed successfully")
            return redirect('profile')
        except OperationalError as e:
            messages.error(request, "please input only vald characters no emojis")
        

    profile = Profile.objects.get(user=request.user)
    context= {"profile":profile}
    return render(request, 'profile/edith_profile.html', context)