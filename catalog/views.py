from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contact_inf(request):
    return render(request, 'catalog/contact_inf.html')
