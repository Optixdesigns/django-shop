# -*- coding: utf-8 -*-
from shop.products.models import Product
from shop.products.forms import ProductForm
from django.views.generic import (TemplateView, ListView, DetailView, View)
from django.views.generic.base import TemplateResponseMixin
from shop.cart.forms import CartItemBaseForm
from django.forms.formsets import formset_factory

class ProductView(DetailView):
	model = Product
	template_name = "shop/product.haml"

	def get_context_data(self, **kwargs):
		context = {
			'add_to_cart_form': CartItemBaseForm(initial={'product_id' : kwargs['object'].id})
		}    

		context.update(kwargs)
		return super(ProductView, self).get_context_data(**context)

class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.haml"