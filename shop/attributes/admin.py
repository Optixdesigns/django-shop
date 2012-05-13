from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from shop.attributes.models import Attribute, Option
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.conf import settings
from django.db import models

class OptionInline(admin.TabularInline):
    model = Option

class AttributeBaseAdmin(admin.ModelAdmin):
	pass

class AttributeAdmin(AttributeBaseAdmin):
	inlines = [
    OptionInline,
  ]
	pass

SHOP_ATTRIBUTE_MODEL = getattr(settings, 'SHOP_ATTRIBUTE_MODEL', None)
if not SHOP_ATTRIBUTE_MODEL:
    admin.site.register(Attribute, AttributeAdmin)