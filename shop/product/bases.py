# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hub.node.models import Node
from shop.utils.fields import CurrencyField
from polymorphic.polymorphic_model import PolymorphicModel
from polymorphic.manager import PolymorphicManager
from autoslug import AutoSlugField
from shop.product.managers import (
    ProductManager,
    ProductStatisticsManager,
)
from datetime import *
from ..utils.models import Subtyped

#==============================================================================
# Product
#==============================================================================
class BaseProduct(Subtyped):
    """
    A basic product for the shop
    Most of the already existing fields here should be generic enough to reside
    on the "base model" and not on an added property
    """
    title      = models.CharField(max_length=255)
    slug       = AutoSlugField(populate_from='title', max_length=255, editable=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    price = CurrencyField(verbose_name=_('Unit price'))

    #objects = ProductManager()
    #statistics = ProductStatisticsManager()

    class Meta(object):
        abstract = True
        app_label = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def get_price(self):
      """
      Return the price for this item (provided for extensibility)
      """
      return self.price

    def get_title(self):
      """
      Return the title of this Product (provided for extensibility)
      """
      return self.title

class VariantBase(Subtyped):
    """
    Base class for variants. It identifies a concrete product instance,
    which goes to a cart. Custom variants inherit from it.
    """
    #objects = PolymorphicManager()
    #objects = PolymorphicManager()

    def form_fields(self):
      return [] 

    def get_title(self):
      """
      Return the title of this Product (provided for extensibility)
      """
      return self.get_subtype_instance().product.title
      
    class Meta:
        abstract = True