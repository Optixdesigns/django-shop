# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from shop.cart.views import CartView, CartAdd

urlpatterns = patterns('',
	url(r'^$', , CartView.as_view(), name='shop_cart'),
    url(r'^add/', CartAdd, name='shop_cart_add'),
)