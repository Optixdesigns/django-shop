# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^products/', include('shop.products.urls')),
    (r'^cart/', include('shop.cart.urls')),
)