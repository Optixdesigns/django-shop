# -*- coding: utf-8 -*-
from shop.cart.models import Cart
from django.views.generic import (TemplateView, ListView, DetailView, View, FormView)
#from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from shop.cart.forms import CartItemBaseForm
from django.forms.formsets import formset_factory


class CartView(ListView):
  template_name = "shop/cart.haml"
  template_name_ajax = "shop/cart_ajax.haml"
  redirect = '/'
  form_class = 'CartItemBaseForm'

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
    
    if hasattr(data, 'form-TOTAL_FORMS'): # formset
      CartItemFormSet = formset_factory(CartItemBaseForm)
      cartitem_formset = CartItemFormSet(request.POST)

      if cartitem_formset.is_valid():
        for form in cartitem_formset:
          form.add_to_cart(request.shop.cart)
    else:
      form = CartItemBaseForm(request.POST)
      if form.is_valid():
        form.add_to_cart(request.shop.cart)    
    
    #if self.request.is_ajax():
          
    #self.render_to_response(*args, **kwargs)
    #super(CartView, self).post(request, *args, **kwargs)
    return self.get(request, *args, **kwargs)
    #return self.get(request, *args, **kwargs)
    #return redirect(self.redirect)  

  def get_context_data(self, **kwargs):
    CartItemFormSet = formset_factory(CartItemBaseForm)
    context = {
      'cartitems_formset': CartItemFormSet()
    }    

    context.update(kwargs)
    return super(CartView, self).get_context_data(**context)