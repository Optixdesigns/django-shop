from django.contrib import admin
from hub.categories.bases import CategoryBase
from hub.categories.models import Category
from hub.categories.utils import *
from django import forms
from django.conf import settings

class CategoryBaseAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  list_display = ('name', 'parent')
  list_filter = ['parent']
  search_fields = ['name']

class CategoryAdmin(CategoryBaseAdmin):
	pass

SHOP_CATEGORY_MODEL = getattr(settings, 'SHOP_CATEGORY_MODEL', None)
if not SHOP_CATEGORY_MODEL:
    admin.site.register(Category, CategoryAdmin)