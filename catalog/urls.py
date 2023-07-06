from catalog.views import home, contact_inf
from django.urls import path

urlpatterns = [
    path('', home),
    path('contacts/', contact_inf)
]
