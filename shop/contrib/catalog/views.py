from django.views.generic import (TemplateView, ListView, DetailView, View)
from shop.products.models import Product
from shop.contrib.catalog.filtersets import *
from shop.contrib.catalog.forms import CatalogForm
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext

def CatalogView(request):
  form = CatalogForm()

  if request.POST:
    data = request.POST.copy()
    form = CatalogForm(data=data)

    #if form.is_valid():
      #form.add_to_cart(request.shop.cart)
      #messages.success(request, 'Product has been added to your cart.')
      #return redirect('shop_cart') # send to cart after adding a product

  return render_to_response('shop/catalog.haml', {'form': form}, context_instance=RequestContext(request))