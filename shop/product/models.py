# -*- coding: utf-8 -*-
"""
This overrides the Product model with the class loaded from the
SHOP_PRODUCT_MODEL setting if it exists.
"""
from django.conf import settings
from django.db import models
from djutils.utils.helpers import load_class

#==============================================================================
# Get the project model
#==============================================================================
PRODUCT_MODEL = getattr(settings, 'SHOP_PRODUCT_MODEL', 'shop.products.defaults.product.Product')
Product = load_class(PRODUCT_MODEL)

VARIANT_MODEL = getattr(settings, 'SHOP_VARIANT_MODEL', 'shop.products.defaults.product.Variant')
Variant = load_class(VARIANT_MODEL)