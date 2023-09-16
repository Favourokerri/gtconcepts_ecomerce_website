from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render
from store.models import Product
# Create your views here.


def index(request):
    featured_products = Product.objects.filter(is_featured=True)
    paginator = Paginator(featured_products, 5)  # Display 5 products per page
    page_number = request.GET.get('page')
    page = paginator.get_page(int(page_number) if page_number else 1)  # Convert to integer and handle None

    context = {'featured_products': page}
    return render(request, 'index.html', context)