from django.shortcuts import render
from store.models import Product, Category

def product_search(request):
    categories = Category.objects.all()
    query = request.GET.get('query')
    category = request.GET.get('category')  # Get the selected category from the form

    results = Product.objects.all()  # Start with all products

    if category:  # If a category is selected, filter by category
        results = results.filter(categories__name=category)
        context = {
            'results': results,
            'categories':categories
        }
        return render(request, 'search.html', context)

    if query:  # If a search query is provided, further filter by name
        results = results.filter(name__icontains=query)

        context = {
            'results': results,
            'categories':categories
        }
        return render(request, 'search.html', context)

    context = {
            'categories':categories
        }
    return render(request, 'search.html', context)
