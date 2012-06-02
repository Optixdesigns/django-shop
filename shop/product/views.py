# -*- coding: utf-8 -*-
from shop.product.models import Product, Variant
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin
from shop.cart.forms import EditCartItemForm, AddToCartForm
from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

def ProductView(request, slug):
  product = get_object_or_404(Product.objects.all(), slug=slug)

  if request.POST:
    data = request.POST.copy()
    form = AddToCartForm(data=data, initial={'product_id': product.id})

    if form.is_valid():
      form.add_to_cart(request.shop.cart)
      messages.success(request, 'Product has been added to your cart.')
      return redirect('shop_cart') # send to cart after adding a product

  else:
    form = AddToCartForm(initial={'product_id': product.id})

  return render_to_response('shop/product.haml', {'object': product, 'add_to_cart_form': form}, context_instance=RequestContext(request))

class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.haml"