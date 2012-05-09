from django.conf.urls.defaults import patterns, url

from shop.cart.views import *
from shop.cart.models import Cart

urlpatterns = patterns('',
    url(r'^$', CartView.as_view(), name='shop_cart_item_list'),
)