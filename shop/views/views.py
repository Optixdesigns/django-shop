# -*- coding: utf-8 -*-
from shop.products.models import Product
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin

class CheckoutView(TemplateView):
    model = Product
    template_name = "shop/checkout/checkout.haml"