from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Homepage',
    }
    return render(request, 'catalog/home.html', context)


def contact_inf(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'catalog/contact_inf.html', context)


def product(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'All categories products',
    }
    return render(request, 'catalog/product.html', context)
