from django.views.generic import (TemplateView, ListView, DetailView, View)
from shop.products.models import Product
from shop.contrib.catalog.filtersets import *

class CatalogView(ListView):
    model = Product
    template_name = "shop/catalog.haml"

    def get_context_data(self, **kwargs):
		context = super(CatalogView, self).get_context_data(**kwargs)
   		context['object_list'] = self.filterset
   		return context

    def get_queryset(self):
    	self.filterset = ProductFilterSet(self.request.GET or None)