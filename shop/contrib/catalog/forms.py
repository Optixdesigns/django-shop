from shop.product.models import Product, Variant
from shop.category.models import Category
from shop.cart.models import CartItem
from shop.cart.bases import BaseCartItem
from django import forms

class CatalogForm(forms.Form):
  q = forms.CharField(label="search", required=False, widget=forms.TextInput(attrs={'placeholder': 'Search term..'}))

  model = Product
  qs = Product.objects.all()

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
      if self.cleaned_data['q']:
        qs = qs.filter(title__icontains=self.cleaned_data['q'])

    return qs