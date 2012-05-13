# -*- coding: utf-8 -*-
"""
This overrides the Product model with the class loaded from the
SHOP_PRODUCT_MODEL setting if it exists.
"""
from django.conf import settings
from django.db import models
from djutils.utils.helpers import load_class

SHOP_ATTRIBUTE_MODEL = getattr(settings, 'SHOP_ATTRIBUTE_MODEL', 'shop.attributes.defaults.attributes.Attribute')
Attribute = load_class(SHOP_ATTRIBUTE_MODEL)

SHOP_ATTRIBUTE_OPTION_MODEL = getattr(settings, 'SHOP_ATTRIBUTE_OPTION_MODEL', 'shop.attributes.defaults.attributes.Option')
Option = load_class(SHOP_ATTRIBUTE_OPTION_MODEL)