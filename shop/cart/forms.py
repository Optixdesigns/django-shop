from shop.products.models import Product, Variant
from shop.cart.models import CartItem
from shop.cart.bases import BaseCartItem
from shop.products.forms import ProductForm
from django import forms
#from django.forms import widgets

class CartItemBaseForm(forms.Form):
  product_id = forms.CharField(widget=forms.widgets.HiddenInput(), required=True)
  quantity = forms.IntegerField(min_value=1, initial=1, required=True, widget=forms.widgets.Select(choices=((1, '1'), (2, '2'), (3, '3'),)))
  variant_fields = []
  variant = None

  def __init__(self, data=None, *args, **kwargs):
    self.product = kwargs.pop('product')
    super(CartItemBaseForm, self).__init__(data=data, *args, **kwargs)
    self.fields['product_id'].initial = self.product.id
    
    # Get variant fields
    for variant in self.product.variants.all():
      self.variant_fields = variant.form_fields() 
      if len(self.variant_fields ) != 0:
        fields = forms.models.fields_for_model(variant, fields=self.variant_fields)
        for name, field in fields.iteritems():
          self.fields[name] = field

    # Set defaults      

  def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    return quantity if quantity is not None else 1

  def clean(self):
    filter_set = {}

    for name in self.variant_fields:
      filter_set[name] = self.cleaned_data.get(name)
    
    qs = self.product.variants.filter(**filter_set)
    if not qs.exists():
      raise forms.ValidationError("Variant does not exist")

    self.cleaned_data['variant'] = qs.get()
    return self.cleaned_data  

  def add_to_cart(self, cart): # make to save
    return cart.add_item(self.cleaned_data['variant'], self.cleaned_data['quantity'])

  def remove_from_cart(self, cart): # make to save
    pass

class AddToCartForm(CartItemBaseForm):
  pass

class EditCartItemForm(CartItemBaseForm):
 #variant = None

  def __init__(self, data=None, *args, **kwargs):
    #print kwargs
    #print kwargs
    #print kwargs['initial']['product_id']
    #initial = kwargs['initial']
    product_id = 1
    #print product_id
    product = Product.objects.get(id=product_id)
    super(EditCartItemForm, self).__init__(data=data, product=product, *args, **kwargs)
