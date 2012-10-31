from django.contrib import admin
from hub.node.admin import NodeAdmin
from hub.node.models import Node
from shop.product.models import Product, Variant
from products.models import *
from shop.product.admin import ProductAdmin
from hub.core.admin import DisplayableAdmin
from sorl.thumbnail.admin import AdminImageMixin
#from shop.models import Product

def enable_featured(modeladmin, request, queryset):
	queryset.update(featured="True")
	enable_featured.short_description = "Enable featured"

def disable_featured(modeladmin, request, queryset):
	queryset.update(featured="False")
	disable_featured.short_description = "Disable featured"

class ProductImageInline(AdminImageMixin, admin.TabularInline):
    model = ProductImage

class SimpleProductAdmin(ProductAdmin):
  extra_fieldsets = ((None, {"fields": ("price", "image", "categories",)}),)
  list_display = ProductAdmin.list_display + ("price", "featured", "status" )
  actions = [enable_featured, disable_featured]   
  inlines = [ProductImageInline,]

  def save_model(self, request, obj, form, change):
    '''
    Save sku an stock level as variant
    '''
    obj.save()
    if obj.variants.exists():
      variant = obj.variants.get()
    else:
      variant = Variant(product=obj)
      variant.stock_level = form.cleaned_data['stock_level']
      variant.sku = form.cleaned_data['sku']
      variant.save()

class PosterVariantInline(admin.TabularInline):
    model = PosterVariant

class PosterAdmin(ProductAdmin):
  extra_fieldsets = ((None, {"fields": ("price", "image", "categories",)}),)
  list_display = ProductAdmin.list_display + ("price", "featured", "status",)
  actions = [enable_featured, disable_featured]   
  inlines = [PosterVariantInline, ProductImageInline,]

class TicketVariantInline(admin.TabularInline):
    model = TicketVariant

class TicketAdmin(ProductAdmin):
  extra_fieldsets = ((None, {"fields": ("price", "image", "categories",)}),)
  list_display = ProductAdmin.list_display + ("price", "featured", "status",)
  actions = [enable_featured, disable_featured]   
  inlines = [TicketVariantInline, ProductImageInline,]

class ClothingVariantInline(admin.TabularInline):
    model = ClothingVariant

class ClothingAdmin(ProductAdmin):
  extra_fieldsets = ((None, {"fields": ("price", "image", "categories",)}),)
  list_display = ProductAdmin.list_display + ("price", "featured", "status",)
  actions = [enable_featured, disable_featured]   
  inlines = [ClothingVariantInline, ProductImageInline,]

admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(SimpleProduct, SimpleProductAdmin)