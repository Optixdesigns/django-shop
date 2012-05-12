# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from djutils.utils.helpers import load_class

#==============================================================================
# Get the category model
#==============================================================================
SHOP_CATEGORY_MODEL = getattr(settings, 'SHOP_CATEGORY_MODEL', 'shop.categories.defaults.category.Category')
Category = load_class(SHOP_CATEGORY_MODEL)