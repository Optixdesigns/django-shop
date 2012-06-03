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
  product_id = forms.CharField(widget=forms.widgets.HiddenInput(), required=True, show_hidden_initial=True)
  variant_id = forms.CharField(widget=forms.widgets.HiddenInput(), required=False)
  quantity = forms.IntegerField(min_value=1, initial=1, required=True, widget=forms.widgets.Select(choices=QUANTITY_CHOICES))
  
  variant = None
  product = None
  variant_field_names = []

  def __init__(self, *args, **kwargs):
    #self.product = product
    #print data
    # we should make this better....
    #variant_id = 
    #self.variant = self._raw_value('product_id')
    '''
    if 'initial' in kwargs and 'variant_id' in kwargs['initial']:
      self.variant = Variant.objects.get(id=kwargs['initial'].get('variant_id'))  
    
    if 'initial' in kwargs and 'product_id' in kwargs['initial']:
      #print kwargs['initial'].get('product_id')
      self.product = Product.objects.get(id=kwargs['initial'].get('product_id'))
    
    # fill in product if not there  
    if self.product is None and self.variant:
      self.product = Product.objects.get(id=self.variant.product.id)
    '''
    #self.fields = copy.deepcopy(self.base_fields)  
    #self.fields = {}

    #print product  
    super(CartItemBaseForm, self).__init__(*args, **kwargs)
    #print kwargs['initial'].get('product_id')
    #print self.fields['quantity'].initial
    #print kwargs['initial'].get('product_id') or self._raw_value('product_id')

    print self.fields['product_id'].value()
    self.add_variant_fields()
    self.get_variant_field_values(*args, **kwargs)
    #print kwargs['data']

    #print self._raw_value('product_id')
    #self.add_variant_fields()
    

    

    #print self.fields['variant_id'].initial
    
    #self._clean_fields()

    
    #print data
    #print args

    #print self.fields['variant_id'].initial

    # Initial field values
    #self.fields['product_id'].initial = self.product.id

    # Buld our fields
    

    #super(CartItemBaseForm, self).__init__(data=data, *args, **kwargs)

    #print _get_existing_variants_choices(product.variants.all(), ('frame', 'size'))
  ''' 
  def add_variant_fields(self):
    fields = forms.models.fields_for_model(variant, fields=variant_field_names)
    for name, field in fields.iteritems():
      self.fields[name] = field

  def add_variant_fields(self):
    fields = forms.models.fields_for_model(variant, fields=variant_field_names)
    for name, field in fields.iteritems():
      self.fields[name] = field    

  '''
  def get_initial_values(self):
    # product_id
    if self._raw_value('product_id'):
      self.fields['product_id'].initial = self._raw_value('product_id')
    elif 'initial' in kwargs and 'product_id' in kwargs['initial']:
      self.fields['product_id'].initial = kwargs['initial'].get('product_id')

    if self._raw_value('variant_id'):
      self.fields['variant_id'].initial = self._raw_value('variant_id')
    elif 'initial' in kwargs and 'variant_id' in kwargs['initial']:
      self.fields['variant_id'].initial = kwargs['initial'].get('variant_id')  




  def add_variant_fields(self):
    # Get product and variant
    product = self.product.get_subtype_instance()

    # Get variant
    if self.variant:
      variant = self.variant.get_subtype_instance()
    else:
      try:
        variant = product.variants.all()[0].get_subtype_instance()
      except:
        return

    # Set variant form fields
    self.variant_field_names = variant.form_fields()

    # Get our form fields and fill in values
    existing_choices = _get_existing_variants_choices(product.variants.all(), variant.form_fields())
    
 
    fields = forms.models.fields_for_model(variant, fields=variant.form_fields())
    #print fields
    for name, field in fields.iteritems():
      self.fields[name] = field
     
    # Only show existing choices  
    for field_name, choices in existing_choices.items():
      for name, field in fields.iteritems():
        self.fields[field_name].widget.choices = choices
   
    # Get defaults for variant fields      
    if variant:
      for name in self.variant_field_names:
        #print name
        self.fields[name].initial = getattr(variant, name)

  def clean_quantity(self):
    quantity = self.cleaned_data['quantity']
    return quantity if quantity is not None else 1

  def clean(self):
    self.extra_answers()

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
