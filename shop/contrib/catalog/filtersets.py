import django_filters
from shop.products.models import Product

class ProductFilterSet(django_filters.FilterSet):
    price = django_filters.NumberFilter(lookup_type='lt')

    class Meta:
        model = Product
        fields = ['title', 'categories', 'price',]