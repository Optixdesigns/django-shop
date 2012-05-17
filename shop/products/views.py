# -*- coding: utf-8 -*-
from shop.products.models import Product, Variant
from shop.products.forms import ProductForm
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin
from shop.cart.forms import EditCartItemForm, AddToCartForm
from django.forms.formsets import formset_factory

class ProductView(DetailView):
  model = Product
  template_name = "shop/product.haml"

  def get_context_data(self, **kwargs):
    product = kwargs['object']
    #print product
    #variant = kwargs['object'].variant_set.all()[0]
    #variant = Variant.objects.filter(product_id=kwargs['object'].id)[0]
    #if product.variants.exists():
      #variant = product.variants.get()
    context = {
      'add_to_cart_form': AddToCartForm(data=None, product=product)
    }    

    context.update(kwargs)
    
    return super(ProductView, self).get_context_data(**context)

class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.haml"