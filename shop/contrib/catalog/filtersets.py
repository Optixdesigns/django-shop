import django_filters
from shop.products.models import Product
from shop.categories.models import Category
from django import forms

class ProductFilterSet(django_filters.FilterSet):
    #price = django_filters.RangeFilter(widget=django_filters.widgets.RangeWidget())
    title = django_filters.CharFilter(label="Search", lookup_type='contains')
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.widgets.Select())

    class Meta:
        model = Product
        order_by = ['price',]
        fields = ['title', 'categories', 'price',]