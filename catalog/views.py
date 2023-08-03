from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Homepage', }

    def get_queryset(self):
        return Product.objects.all()[:3]


def contact_inf(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'catalog/contact_inf.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {'title': 'All categories products', }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
