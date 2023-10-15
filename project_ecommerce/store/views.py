from django.shortcuts import render
from store.models import Category, Product
# Create your views here.

def products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'categories': category}
    return render(request, 'main/shop.html', context)