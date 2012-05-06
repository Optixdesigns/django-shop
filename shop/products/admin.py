from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node

class BaseProductAdmin(NodeAdmin):
	extra_fieldsets = ((None, {"fields": ("unit_price",)}),)
	pass
