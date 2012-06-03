from shop.product.models import Product, Variant
from shop.cart.models import CartItem
from shop.cart.bases import BaseCartItem
from django import forms
import copy

def _get_existing_variants_choices(queryset, field_names):
    field2choices = {}
    variants = queryset.values_list(*field_names)

    if variants:
        for index, existing_choices in enumerate(zip(*variants)):
            field_name = field_names[index]
            all_choices = queryset.model._meta.get_field(field_name).choices
            field2choices[field_name] = [c for c in all_choices if c[0] in existing_choices]
    else:
        for field_name in field_names:
            field2choices[field_name] = []
    return field2choices

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

  def __init__(self, *args, **kwargs):
    super(CartItemBaseForm, self).__init__(*args, **kwargs)
    self.product = self.get_product()
    self.variant = self.get_variant()
    self.add_variant_fields()

  def get_product(self):
    product_id = self.__getitem__('product_id').value()
    product = Product.objects.get(id=product_id).get_subtype_instance()
    return product

  def get_variant(self):
    variant_id = self.__getitem__('variant_id').value()
    try:
      variant = Variant.objects.get(id=variant_id).get_subtype_instance()
      return variant
    except:
      return None

  def add_variant_fields(self):
    # Get variant for its fields
    #print self.product
    #print self.product.variants.all()
    if self.variant:
      variant = self.variant
    else:
      variant = self.product.variants.all()[0].get_subtype_instance()

    # Set variant form fields
    self.variant_field_names = variant.form_fields()

    # Get our form fields and fill in values
    existing_choices = _get_existing_variants_choices(self.product.variants.all(), variant.form_fields())

    fields = forms.models.fields_for_model(variant, fields=variant.form_fields())

    for name, field in fields.iteritems():
      self.fields[name] = field
     
    # Only show existing choices  
    for field_name, choices in existing_choices.items():
      for name, field in fields.iteritems():
        self.fields[field_name].widget.choices = choices
   
    # Get defaults for variant fields      
    if variant:
      for name in self.variant_field_names:
        self.fields[name].initial = getattr(variant, name)

  def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    return quantity if quantity is not None else 1

  def clean(self):
    filter_set = {}

    for name in self.variant_field_names:
      filter_set[name] = self.cleaned_data.get(name)
      
    product = self.product.get_subtype_instance()
    qs = product.variants.filter(**filter_set)
    if not qs.exists():
      raise forms.ValidationError("Variant does not exist")

    self.cleaned_data['variant'] = qs.get()
    return self.cleaned_data  

  def add_to_cart(self, cart): # make to save
    return cart.add_item(self.cleaned_data['variant'], self.cleaned_data['quantity'])

class AddToCartForm(CartItemBaseForm):
  pass

class EditCartItemForm(CartItemBaseForm):
  pass
