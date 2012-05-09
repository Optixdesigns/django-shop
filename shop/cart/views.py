# -*- coding: utf-8 -*-
from shop.cart.models import Cart
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin

class CartView(DetailView):
    model = Cart