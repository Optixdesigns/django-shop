# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from shop.cart.views import CartView

urlpatterns = patterns('',
	url(r'^$', 'shop.cart.views.CartView', name='shop_cart'),
    url(r'^add/$', 'shop.cart.views.AddToCartView', name='shop_cart_add'),
)