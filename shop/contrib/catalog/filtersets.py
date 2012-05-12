import django_filters
from shop.products.models import Product

class ProductFilterSet(django_filters.FilterSet):
    price = django_filters.NumberFilter(lookup_type='lt')
    title = django_filters.CharFilter(label="Search")

    class Meta:
        model = Product
        fields = ['title', 'categories', 'price',]