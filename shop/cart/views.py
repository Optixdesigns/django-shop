# -*- coding: utf-8 -*-
from shop.cart.models import Cart, CartItem
from django.views.generic import (TemplateView, ListView, DetailView, View, FormView, RedirectView, UpdateView)
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from shop.cart.forms import EditCartItemForm, AddToCartForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory 
from shop.product.models import Product, Variant
from django.utils import simplejson
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

def AddToCartView(request):
  if not request.POST:
    return

  data = request.POST.copy()
  success = True

  if hasattr(data, 'form-TOTAL_FORMS'):
    AddToCartFormSet = formset_factory(AddToCartForm)
    addtocart_formset = AddToCartFormFormSet(data)

    if addtocart_formset.is_valid():
      for form in addtocart_formset:
        form.add_to_cart(request.shop.cart)
    else:
      success = False     
  else:
    product = Product.objects.get(id=data['product_id'])
    form = AddToCartForm(data=data, product=product)

    if form.is_valid():
      form.add_to_cart(request.shop.cart)
    else:
      success = False  
  
  if request.is_ajax():
    return HttpResponse(simplejson.dumps({"success": success}), mimetype='application/javascript')
  
  return redirect('shop_cart')

def CartView(request):
  template = "shop/cart.haml"
  EditCartItemFormSet = formset_factory(EditCartItemForm, extra=0, can_delete=True)

  if request.POST:
    formset = EditCartItemFormSet(request.POST)

    if formset.is_valid():
      for form in formset:
        request.shop.cart.update_item(form.cleaned_data['variant'], form.cleaned_data['quantity'], form.variant)
        #form.add_to_cart(request.shop.cart)
  else:
    initial = []
    for item in request.shop.cart.items.all():
      variant = item.variant.get_subtype_instance()
      initial.append({
        'product': variant.product,
        'variant': variant,
        'variant_id': variant.id,
        'product_id': variant.product.id,
        'quantity': item.quantity,
      })

    formset = EditCartItemFormSet(initial=initial)

  if request.is_ajax():
    template = "shop/cart_ajax.haml"

  return render_to_response(template, {'formset': formset}, context_instance=RequestContext(request))    

'''
class CartView(TemplateView, RedirectView):
  template_name = "shop/cart.haml"
  template_name_ajax = "shop/cart_ajax.haml"
  redirect = '/'

  def get_template_names(self):
    if self.request.is_ajax():
      self.template_name = self.template_name_ajax

    return super(CartView, self).get_template_names()
  
  def get_queryset(self):
    return self.request.shop.cart.items.all()

  def post(self, request, *args, **kwargs):
    data = request.POST.copy()
    
    if hasattr(data, 'form-TOTAL_FORMS'):
      EditCartItemFormSet = formset_factory(EditCartItemForm)
      cartitem_formset = EditCartItemFormSet(request.POST)

      if cartitem_formset.is_valid():
        for form in cartitem_formset:
          form.add_to_cart(request.shop.cart)
    else:
      product = Product.objects.get(id=data['product_id'])
      form = EditCartItemForm(data=data, product=product)

      if form.is_valid():
        form.add_to_cart(request.shop.cart) 
    
    return self.get(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    initial = []
    for item in self.request.shop.cart.items.all():
      #variant = item.variant.get_subtype_instance()
      variant = item.variant.get_subtype_instance()
      initial.append({
        'product_id': variant.product.id, 
        'variant_id': variant.id, 
        'quantity': item.quantity,
      })
    

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
'''