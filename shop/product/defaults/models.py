# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from shop.products.bases import BaseProduct, VariantBase
from hub.core.models import Featurable, Displayable, Orderable, RichText

class Product(BaseProduct):
	class Meta(object):
		abstract = False
		app_label = 'products'
		verbose_name = _('Product')
		verbose_name_plural = _('Products')
		db_table = 'shop_products_product'

class Variant(VariantBase):
	class Meta(object):
		abstract = False
		app_label = 'products'