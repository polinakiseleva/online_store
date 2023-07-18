from catalog.apps import CatalogConfig
from catalog.views import home, contact_inf, product
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact_inf, name='contacts'),
    path('product/', product, name='product'),
]
