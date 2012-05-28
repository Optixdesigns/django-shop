from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from shop.product.models import Product
from hub.core.admin import DisplayableAdmin
from django.conf import settings

class ProductBaseAdmin(admin.ModelAdmin):
	pass

class ProductAdmin(ProductBaseAdmin):
	pass

SHOP_PRODUCT_MODEL = getattr(settings, 'SHOP_PRODUCT_MODEL', None)
if not SHOP_PRODUCT_MODEL:
    admin.site.register(Product, ProductAdmin)