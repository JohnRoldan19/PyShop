# products/views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)

def product_detail(request, product_id):
    # Define this view if it's referenced in urls.py
    pass

def new(request):
    # Define this view if it's referenced in urls.py
    pass
