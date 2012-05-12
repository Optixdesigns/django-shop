from django.contrib import admin
from hub.categories.bases import CategoryBase
from hub.categories.models import Category
from hub.categories.utils import *
from django import forms

class CategoryBaseAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  list_display = ('name', 'parent')
  list_filter = ['parent']
  search_fields = ['name']

class CategoryAdmin(CategoryBaseAdmin):
  prepopulated_fields = {"slug": ("name",)}
  list_display = ('name', 'parent')
  list_filter = ['parent']
  search_fields = ['name']

admin.site.register(Category, CategoryAdmin)