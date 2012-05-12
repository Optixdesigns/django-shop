# -*- coding: utf-8 -*-
from shop.cart.models import Cart
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from shop.cart.forms import CartItemForm

class CartView(ListView):
  template_name = "shop/cart.haml"

  def get_queryset(self):
    return self.request.shop.cart.items.all()

  def post(self, request, *args, **kwargs):
    form = CartItemForm(request.POST)
    if form.is_valid():
        form.add_to_cart(request.cart)
        if request.is_ajax():
            return HttpResponse(status=201)
        
        return redirect('shop_cart_item_list')
    
    return HttpResponseBadRequest()