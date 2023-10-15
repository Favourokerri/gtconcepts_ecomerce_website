from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from store.models import Product
from blog_app.models import Blog_Post
# Create your views here.


def index(request):
    """ contains featured post from:
        product, blog.
    """
    featured_products = Product.objects.filter(is_featured=True)
    featured_blogs = Blog_Post.objects.filter(is_featured=True)
    context = {'featured_products': featured_products,
               'featured_blogs': featured_blogs}

    return render(request, 'main/index.html', context)


def custom_404_view(request, exception):
    return render(request, 'error/404.html', status=404)

def custom_500_view(request, exception):
    return render(request, 'error/500.html', status=500)
