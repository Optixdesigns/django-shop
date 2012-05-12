from django.conf.urls.defaults import patterns, url

from shop.contrib.catalog.views import CatalogView
#from shop.cart.models import Cart

urlpatterns = patterns('',
    url(r'^$', CatalogView.as_view(), name='shop_catalog'),
)