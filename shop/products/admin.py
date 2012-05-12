from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from shop.products.models import Product
from hub.core.admin import DisplayableAdmin

class ProductAdmin(DisplayableAdmin):
	pass

admin.site.register(Product, ProductAdmin)