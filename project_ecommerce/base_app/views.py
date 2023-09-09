from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from catalog.models import Product
# Create your views here.


def index(request):
    featured_products = Product.objects.filter(is_featured=True)
    context = {'featured_products': featured_products}
    return render(request, 'index.html', context)