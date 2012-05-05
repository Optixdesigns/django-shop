from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from shop.products.models import Product

#extra_fieldsets = ((None, {"fields": ("image",)}),)

class ProductAdmin(NodeAdmin):
	#extra_fieldsets = ((None, {"fields": ("image",)}),)
	#print ArticleAdmin.fieldsets
	#fieldsets = deepcopy(ArticleAdmin.fieldsets) + extra_fieldsets
	#print fieldsets
	pass

admin.site.register(Product, ProductAdmin)