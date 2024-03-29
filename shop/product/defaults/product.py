# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from shop.products.bases import BaseProduct
from hub.core.models import Featurable, Displayable, Orderable, RichText

class Product(Displayable, Featurable, RichText, BaseProduct):
	class Meta(object):
		abstract = False
		app_label = 'products'
		verbose_name = _('Product')
		verbose_name_plural = _('Products')
		db_table = 'shop_products_product'