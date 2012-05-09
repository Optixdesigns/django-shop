# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
#from shop.cart.models import CART_MODEL
from shop.utils.helpers import get_model_string
from shop.cart.managers import CartManager

class BaseCart(models.Model):
    """
    This should be a rather simple list of items. Ideally it should be bound to
    a session and not to a User is we want to let people buy from our shop
    without having to register with us.
    """
    # If the user is null, that means this is used for a session
    user = models.OneToOneField(User, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CartManager()

    class Meta(object):
        abstract = True
        app_label = 'cart'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def add(self, product, quantity=1):
      """
      Add or update a cart item
      """
      item, created = self.items.get_or_create(
          product = product,
          defaults = {'quantity': quantity,},
      )
      if not created:
          item.quantity += quantity
          item.save()
      #self.reset_cached_items()
      return item

class BaseCartItem(models.Model):
    """
    This is a holder for the quantity of items in the cart and, obviously, a
    pointer to the actual Product being purchased :)
    """
    cart = models.ForeignKey(get_model_string('Cart'), related_name="items")
    quantity = models.IntegerField()
    product = models.ForeignKey(get_model_string('Product'))

    class Meta(object):
        abstract = True
        app_label = 'cart'
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')