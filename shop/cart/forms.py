from shop.products.models import Product
from django import forms

class CartItemForm(forms.Form):
  product_id = forms.IntegerField(min_value=1)
  quantity = forms.IntegerField(min_value=1, initial=1, required=False)

  def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    return quantity if quantity is not None else 1

  def clean(self):
    product_id = self.cleaned_data.get('product_id')
    if product_id:
      try:
        product = Product.objects.get(pk=product_id)
      except:
        raise forms.ValidationError('Error occured adding to your cart')

      self.cleaned_data['product'] = product

    return self.cleaned_data

  def add_to_cart(self, cart):
    return cart.add(self.cleaned_data['product'], self.cleaned_data['quantity'])