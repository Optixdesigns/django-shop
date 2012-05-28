# -*- coding: utf-8 -*-
"""
This overrides the Address model with the class loaded from the
SHOP_PRODUCT_MODEL setting if it exists.
"""
from django.conf import settings
from django.db import models
from djutils.utils.helpers import load_class

#==============================================================================
# Get the project model
#==============================================================================
ADDRESS_MODEL = getattr(settings, 'SHOP_ADDRESS_MODEL', 'shop.address.defaults.models.Address')
Address = load_class(ADDRESS_MODEL)