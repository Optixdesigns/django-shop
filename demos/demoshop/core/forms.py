from shop.product.models import Product, Variant
from shop.category.models import Category
from shop.contrib.catalog.forms import CatalogForm
from django.utils.translation import ugettext_lazy as _
from django import forms

class CatalogForm(CatalogForm):
  #categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, widget=forms.widgets.CheckboxSelectMultiple())
  frame_color = forms.MultipleChoiceField(choices=(('unframed', _("Unframed")), ('black', _("Black Frame")),), required=False, widget=forms.widgets.CheckboxSelectMultiple())
  sorting = forms.ChoiceField(choices=(('unframed', _("Price: Low to High")), ('black', _("Price: High to low")), ('black', _("By name")),), required=False, label="Sort by",)


  def results(self):
    print self.initial
    qs = super(CatalogForm, self).results()
    #print qs
    return qs