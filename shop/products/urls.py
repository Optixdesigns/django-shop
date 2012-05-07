from django.conf.urls.defaults import patterns, url

from shop.products.views import *
from shop.products.models import Product

urlpatterns = patterns('',
    url(r'^$',
        ProductListView.as_view(),
        name='product_list'
        ),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$',
        ProductDetailView.as_view(),
        name='product_detail'
        ),
    )