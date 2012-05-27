from shop.products.models import Product, Variant
from shop.categories.models import Category
from shop.cart.models import CartItem
from shop.cart.bases import BaseCartItem
from django import forms

class CatalogForm(forms.Form):
  model = Product
  qs = None

  def __init__(self, data=None, *args, **kwargs):
  	if 'qs' in kwargs:
  		self.qs = kwargs['qs']
  	else:
  		self.qs = self.model.objects.all()	

  	super(CatalogForm, self).__init__(data=data, *args, **kwargs)

  def results(self):
  	return self.qs