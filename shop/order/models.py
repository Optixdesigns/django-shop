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
ORDER_MODEL = getattr(settings, 'SHOP_ORDER_MODEL', 'shop.order.defaults.models.Order')
Order = load_class(ORDER_MODEL)