from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'shop.contrib.catalog.views.CatalogView', name='shop_catalog'),
)