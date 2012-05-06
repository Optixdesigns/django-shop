# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hub.node.models import Node
from shop.utils.fields import CurrencyField

#==============================================================================
# Product
#==============================================================================
class BaseProduct(Node):
    """
    A basic product for the shop
    Most of the already existing fields here should be generic enough to reside
    on the "base model" and not on an added property
    """

    sku = models.CharField(max_length=255)

    class Meta(object):
        abstract = True
        app_label = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def get_price(self):
        """
        Return the price for this item (provided for extensibility)
        """
        return self.unit_price

    def get_title(self):
        """
        Return the title of this Product (provided for extensibility)
        """
        return self.title

class ProductPrice(models.Model):
    price = CurrencyField(verbose_name=_('Unit price'))
    pass