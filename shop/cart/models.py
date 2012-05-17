# -*- coding: utf-8 -*-
"""
This overrides the Cart model with the class loaded from the
SHOP_CART_MODEL setting if it exists.
"""
from django.conf import settings
from django.db import models
from djutils.utils.helpers import load_class

#==============================================================================
# Get the project model
#==============================================================================
SHOP_CART_MODEL = getattr(settings, 'SHOP_CART_MODEL', 'shop.cart.defaults.models.Cart')
Cart = load_class(SHOP_CART_MODEL)

SHOP_CARTITEM_MODEL = getattr(settings, 'SHOP_CARTITEM_MODEL', 'shop.cart.defaults.models.CartItem')
CartItem = load_class(SHOP_CARTITEM_MODEL)