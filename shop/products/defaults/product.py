# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from shop.products.bases import BaseProduct
from shop.products.managers import (
    ProductManager,
    ProductStatisticsManager,
)

class Product(BaseProduct):
    objects = ProductManager()
    statistics = ProductStatisticsManager()

    class Meta(object):
        abstract = False
        app_label = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')