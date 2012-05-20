# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from shop.products.views import ProductView

urlpatterns = patterns('',
	url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', ProductView, name='shop_product'),
)