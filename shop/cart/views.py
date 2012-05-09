# -*- coding: utf-8 -*-
from shop.cart.models import Cart
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin

class CartView(ListView):
  template_name = "shop/cart.haml"

  def get_queryset(self):
    return self.request.cart.items.all()