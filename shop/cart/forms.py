from shop.products.models import Product
from shop.cart.bases import BaseCartItem
from django import forms
#from django.forms import widgets

class CartItemBaseForm(forms.Form):
  product_id = forms.CharField(widget=forms.widgets.HiddenInput(), required=True)
  quantity = forms.IntegerField(min_value=1, initial=1, required=True, widget=forms.widgets.Select(choices=((1, '1'), (2, '2'), (3, '3'),)))

  #class Meta:
    #model = BaseCartItem

  def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    return quantity if quantity is not None else 1

  def clean(self):
    #print "clean"
    product_id = self.cleaned_data.get('product_id')
    if product_id:
      try:
        product = Product.objects.get(pk=product_id)
      except:
        raise forms.ValidationError('Error occured adding to your cart')

      self.cleaned_data['product'] = product

    return self.cleaned_data

  def add_to_cart(self, cart):
    return cart.add_product(self.cleaned_data['product'], self.cleaned_data['quantity'])