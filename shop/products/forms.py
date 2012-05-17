from shop.products.models import Product, Variant
from core.models import PosterVariant
from django import forms
from django.db.models import Q

class ProductForm(forms.Form):
  product = None
  variant_fields = []

  def __init__(self, data=None, product=None, *args, **kwargs):
    self.product = product
    #self.variant_model = self.product.get_variant_model()
    #print self.product.get_variant()
    #print Variant.objects.select_subclasses().filter(frame="unframed")
    #print Variant.objects.get_subclass(frame="unframed")
    super(ProductForm, self).__init__(data=data, *args, **kwargs)
    for variant in self.product.variants.all():
      #print variant
      self.variant_fields = variant.form_fields() 
      if len(self.variant_fields ) != 0:
        fields = forms.models.fields_for_model(variant, fields=self.variant_fields)
        for name, field in fields.iteritems():
          self.fields[name] = field

  def clean(self):
    if not self._get_variant_queryset().exists():
      raise forms.ValidationError("Variant does not exist")
    
    return self.cleaned_data
  
  def _get_variant_queryset(self):
    #filter_set = {'product_id': self.product.id}
    filter_set = {}
    
    #print self.product
    for name in self.variant_fields:
      filter_set[name] = self.cleaned_data.get(name)

    #print self.product
    #print self.product.variants.all()
    #if self.product.variants.exists():
      #variant = self.product.variants.get()
    

    #print self.product.variants
    #print variant.frame
      #variantmodel = variant._meta.object_name
    #print variant._meta.object_name
    #variant_model = self.product.get_variant_model()  
    #print variantmodel.objects.get(frame="unframed") 
    #print filter_set  
    #print Variant.objects.filter(Q(frame="unframed"))
    #print Variant.objects.filter(Q(frame="unframed"))
    #print self.product._meta.object_name
    #print Variant.objects.get(frame="unframed")
    #print Product.objects.filter(sku="1241214")
    #print Variant.objects.filter(frame="unframed")
    #print self.variant_model = 
    #print self.product.variants.instance_of(self.variant_model).filter(filter_set)
    #return self.product.variants.instance_of(self.variant_mode).filter(filter_set)
    return self.product.variants.filter(filter_set)

  def get_variant(self):
    return self._get_variant_queryset().get()


class VariantForm(forms.ModelForm):
  model = Variant
  
  '''
  def __init__(self, data=None, *args, **kwargs):
    self.product = kwargs.pop('product')
    super(CartItemBaseForm, self).__init__(data=data, *args, **kwargs)
    for variant in self.product.variants.all():
      variant_fields = variant.form_fields() 
      if len(variant_fields) != 0:
        fields = forms.models.fields_for_model(variant, fields=variant_fields)
        for name, field in fields.iteritems():
          self.fields[name] = field
  pass
  '''