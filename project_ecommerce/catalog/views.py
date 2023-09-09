from django.shortcuts import render
from catalog.models import Category, Product
# Create your views here.

def products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'categories': category}
    return render(request, 'shop.html', context)
