# -*- coding: utf-8 -*-
from shop.cart.models import Cart, CartItem
from django.views.generic import (TemplateView, ListView, DetailView, View, FormView, RedirectView, UpdateView)
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from shop.cart.forms import EditCartItemForm, AddToCartForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory 
from shop.products.models import Product, Variant

'''
class CartView(request):
  data = request.POST.copy()

  form = AddToCartForm(data)
  if form.is_valid():
    form.add_to_cart(request.shop.cart)
  
  redirect('shop/cart/')
'''
class AddToCartView(TemplateView, RedirectView):
  pass


class CartView(TemplateView, RedirectView):
  template_name = "shop/cart.haml"
  template_name_ajax = "shop/cart_ajax.haml"
  redirect = '/'

  def get_template_names(self):
    '''
    Show ajax version if needed
    '''
    if self.request.is_ajax():
      self.template_name = self.template_name_ajax

    return super(CartView, self).get_template_names()
  
  def get_queryset(self):
    return self.request.shop.cart.items.all()

  def post(self, request, *args, **kwargs):
    data = request.POST.copy()
    #print data
    
    if hasattr(data, 'form-TOTAL_FORMS'):
      EditCartItemFormSet = formset_factory(EditCartItemForm)
      cartitem_formset = EditCartItemFormSet(request.POST)

      if cartitem_formset.is_valid():
        for form in cartitem_formset:
          form.add_to_cart(request.shop.cart)
    else:
      product = Product.objects.get(id=data['product_id'])
      form = EditCartItemForm(data=data, product=product)
      #print "yo"
      if form.is_valid():
        #print "go"
        form.add_to_cart(request.shop.cart)
      #print form.errors  
    
    return self.get(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    initial = []
    for item in self.request.shop.cart.items.all():
      #variant = item.variant.get_subtype_instance()
      variant = item.variant.get_subtype_instance()
      initial.append({'product_id': variant.product.id, 'quantity': item.quantity,})
    
    #print initial
    CartItemFormSet = formset_factory(EditCartItemForm, extra=0, can_delete=True)
    context = {
      'cartitems_formset': CartItemFormSet(initial=initial)
    }
    #print CartItemFormSet(queryset=self.request.shop.cart.items.all())
    #return context
    context.update(kwargs)
    return context
    #print context
    return super(CartView, self).get_context_data(**context)