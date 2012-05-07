from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from shop.products.models import Product

class BaseProductAdmin(NodeAdmin):
	extra_fieldsets = ((None, {"fields": ("price",)}),)
	list_display = NodeAdmin.list_display + ("price",)
	pass

class ProductAdmin(BaseProductAdmin):
	pass

admin.site.register(Product, ProductAdmin)

