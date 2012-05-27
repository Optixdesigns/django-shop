from shop.products.models import Product, Variant
from shop.categories.models import Category
from shop.cart.models import CartItem
from shop.cart.bases import BaseCartItem
from django import forms

class CatalogForm(forms.Form):
  q = forms.CharField(label="search")

  model = Product
  qs = None

  def __init__(self, data=None, *args, **kwargs):
  	if 'qs' in kwargs:
  		self.qs = kwargs['qs']
  	else:
  		self.qs = self.model.objects.all()	

  	super(CatalogForm, self).__init__(data=data, *args, **kwargs)

  def results(self):
    qs = self.qs

    if hasattr(self, 'cleaned_data'):
      data = self.cleaned_data

      # Search string
      if data.get('q'):
        qs = qs.filter(title=data.get('q'))

  	return qs