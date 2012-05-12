# -*- coding: utf-8 -*-
from shop.products.models import Product
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin

class ProductView(DetailView):
    model = Product
    template_name = "shop/product.haml"

class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.haml"