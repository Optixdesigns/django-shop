from shop.products.models import Product, Variant
from shop.cart.models import CartItem
from shop.cart.bases import BaseCartItem
from django import forms

choices = {}
for x in range(30):
  choices[x] = x

QUANTITY_CHOICES = tuple(choices.items())

class CartItemBaseForm(forms.Form):
  product_id = forms.CharField(widget=forms.widgets.HiddenInput(), required=True)
  variant_id = forms.CharField(widget=forms.widgets.HiddenInput(), required=False)
  quantity = forms.IntegerField(min_value=1, initial=1, required=True, widget=forms.widgets.Select(choices=QUANTITY_CHOICES))
  
  variant = None
  product = None
  variant_field_names = []

  def __init__(self, data=None, *args, **kwargs):
    if 'initial' in kwargs and 'variant' in kwargs['initial']:
      self.variant = kwargs['initial'].get('variant')
      self.product = self.variant.product
      kwargs['initial']['variant_id'] = self.variant.id
      kwargs['initial']['product_id'] = self.variant.product.id
    else:
      if 'product' in kwargs:
        self.product = kwargs.pop('product')
        #self.product = kwargs.pop('product')

    super(CartItemBaseForm, self).__init__(data=data, *args, **kwargs)

    # Initial field values
    self.fields['product_id'].initial = self.product.id
    #if self.variant:
      #self.fields['variant_id'].initial = self.variant.id
    
    # Get variant fields
    for variant in self.product.variants.all():
      variant =  variant.get_subtype_instance()
      self.variant_field_names = variant.form_fields()
      if len(self.variant_field_names ) != 0:
        fields = forms.models.fields_for_model(variant, fields=self.variant_field_names)
        for name, field in fields.iteritems():
          self.fields[name] = field

    # Get defaults for variant fields      
    if self.variant:
      for name in self.variant_field_names:
        self.fields[name].initial = getattr(self.variant, name)

  def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    return quantity if quantity is not None else 1

  def clean(self):
    filter_set = {}

    for name in self.variant_field_names:
      filter_set[name] = self.cleaned_data.get(name)
    
    qs = self.product.variants.filter(**filter_set)
    if not qs.exists():
      raise forms.ValidationError("Variant does not exist")

    self.cleaned_data['variant'] = qs.get()
    return self.cleaned_data  

  def add_to_cart(self, cart): # make to save
    return cart.add_item(self.cleaned_data['variant'], self.cleaned_data['quantity'])

class AddToCartForm(CartItemBaseForm):
  pass

class EditCartItemForm(CartItemBaseForm):
 #variant = None

  def __init__(self, data=None, *args, **kwargs):
    #print kwargs
    #print kwargs
    #print kwargs['initial']['product_id']
    #initial = kwargs['initial']
    #product_id = 1
    #product = Product.objects.get(id=product_id)
    #product = None
    #if 'initial' in kwargs and 'product_id' in kwargs['initial']:
      #product = Product.objects.get(id=kwargs['initial'].get('product_id'))

    super(EditCartItemForm, self).__init__(data=data, *args, **kwargs)
