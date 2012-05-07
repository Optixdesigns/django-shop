# -*- coding: utf-8 -*-
from shop.products.models import Product
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin

class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product