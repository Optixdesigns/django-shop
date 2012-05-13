# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from shop.utils.fields import CurrencyField
from polymorphic.polymorphic_model import PolymorphicModel
from shop.utils.helpers import get_model_string

#==============================================================================
# Product
#==============================================================================
class AttributeBase(PolymorphicModel):
    name      = models.CharField(max_length=255)
    #product = models.ForeignKey(get_model_string('Product'), related_name="Attributes")
    #products = models.ManyToManyField(get_model_string('Product'), blank=True, null=True)

    class Meta(object):
        abstract = True
        app_label = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return self.name

class OptionBase(PolymorphicModel):
    attribute = models.ForeignKey(get_model_string('Attribute'), related_name="options")
    name      = models.CharField(max_length=255)
    price = CurrencyField(verbose_name=_('Unit price'))

    class Meta(object):
        abstract = True

    def __unicode__(self):
        return self.name

'''
class ProductAttribute(models.Model):
    attribute = models.ForeignKey(Attribute)
    product = models.ForeignKey(Product)
    #price = models.CharField(max_length=128)
'''  