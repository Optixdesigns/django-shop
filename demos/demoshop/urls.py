from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import IndexView
#from shop import urls as shop_urls
from django.conf import settings
from shop.product.views import *
from shop.cart.views import CartView
from shop.cart.forms import AddToCartForm
#from shop_simplevariations import urls as simplevariations_urls

# Admin
admin.autodiscover()

# SEO
#from rollyourown.seo.admin import register_seo_admin
#from core.seo import SiteMetadata
#register_seo_admin(admin.site, SiteMetadata)

urlpatterns = patterns('',
	(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^share/', include('share.urls')),

    url(r'^$', IndexView.as_view(), name='home'),

    # shop
    #(r'^shop/', include('shop.urls')),
    #url(r'^product/(?P<slug>[0-9A-Za-z-_.//]+)/$', ProductView.as_view(), name='shop_product'),
    #url(r'^cart/$', CartView.as_view(), name='shop_cart'),
    url(r'^catalog/$', 'core.views.CatalogView', name='shop_catalog'),
    url(r'^catalog/(?P<category_slug>[a-zA-Z0-9-_]+)/$', 'core.views.CatalogView', name='shop_catalog'),
    (r'^product/', include('shop.product.urls')),
    (r'^cart/', include('shop.cart.urls')),

    (r'^ajax/form_validation/$', 'ajax_validation.views.validate', {'form_class': AddToCartForm}, 'contact_form_validate')
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
  urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
  )