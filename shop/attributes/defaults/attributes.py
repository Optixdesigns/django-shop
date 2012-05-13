# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from shop.attributes.bases import *

class Attribute(AttributeBase):
	class Meta(object):
		abstract = False
		app_label = 'attributes'
		verbose_name = _('Attribute')
		verbose_name_plural = _('Attributes')
		db_table = 'shop_attributes_attribute'

class Option(OptionBase):
	class Meta(object):
		abstract = False
		app_label = 'attributes'
		verbose_name = _('Option')
		verbose_name_plural = _('Options')
		db_table = 'shop_attributes_option'		