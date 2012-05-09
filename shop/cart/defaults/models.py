# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from shop.cart.bases import *

class Cart(BaseCart):
    class Meta(object):
        abstract = False
        app_label = 'cart'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
        db_table = 'shop_cart_cart'

class CartItem(BaseCartItem):
    class Meta(object):
        abstract = False
        app_label = 'cart'
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')
        db_table = 'shop_cart_cart_item'       