# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
#from shop.cart.models import CART_MODEL
from shop.utils.helpers import get_model_string
from shop.cart.managers import CartManager
from django.utils.datastructures import SortedDict
from decimal import Decimal

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

    def __init__(self, *args, **kwargs):
      super(BaseCart, self).__init__(*args, **kwargs)
      # That will hold things like tax totals or total discount
      self.subtotal_price = Decimal('0.0')
      self.total_price = Decimal('0.0')
      #self.current_total = Decimal('0.0')  # used by cart modifiers
      self.modifiers = SortedDict()
      #self.extra_price_fields = []  # List of tuples (label, value)
      #self._updated_cart_items = None
      self.update()

    objects = CartManager()

    def add_item(self, variant, quantity=1):
      """
      Add or update a cart item
      """
      item, created = self.items.get_or_create(
          variant = variant,
          defaults = {'quantity': quantity,},
      )

      if not created:
        item.quantity += quantity
        item.save()

      self.save() # Save to update cart item dates
      return item

    def update_item(self, variant, quantity=1):
      """
      Add or update a cart item
      """
      item, created = self.items.get_or_create(
          variant = variant,
          defaults = {'quantity': quantity,},
      )

      if not created:
        item.quantity += quantity
        item.save()

      self.save() # Save to update cart item dates
      return item

    def update(self):
      '''
      Update cart
      '''
      self.subtotal_price = Decimal('0.0')  # Reset the subtotal
      self.total_price = Decimal('0.0')  # Reset the total price

      for item in self.items.all():
        self.subtotal_price += item.line_total
      
      #for modifier in get_cart_modifiers():
          #total_price = modifier(self, total_price)
      #print self.subtotal_price
      self.total_price = self.subtotal_price

    def clear(self):
      """
      Remove a carts content
      """
      self.items.all().delete()
      #self.modifiers.clear()

    class Meta(object):
      abstract = True
      app_label = 'cart'
      verbose_name = _('Cart')
      verbose_name_plural = _('Carts')

class BaseCartItem(models.Model):
    """
    This is a holder for the quantity of items in the cart and, obviously, a
    pointer to the actual Product being purchased :)
    """
    cart = models.ForeignKey(get_model_string('Cart'), related_name="items")
    quantity = models.IntegerField()
    #product = models.ForeignKey(get_model_string('Product'))
    variant = models.ForeignKey(get_model_string('Variant'))

    def __init__(self, *args, **kwargs):
      super(BaseCartItem, self).__init__(*args, **kwargs)
      self.line_subtotal = Decimal('0.0')
      self.line_total = Decimal('0.0')

      #self.update()
      #self.current_total = Decimal('0.0')  # Used by cart modifiers

    def update(self):
      '''
      Update cart item
      '''
      self.line_subtotal = self.product.get_price() * self.quantity
      self.current_total = self.line_subtotal
      #print self.product.get_price()
      #print self.current_total
      #for modifier in cart_modifiers_pool.get_modifiers_list():
      # We now loop over every registered price modifier,
      # most of them will simply add a field to extra_payment_fields
      #modifier.process_cart_item(self, state)

      self.line_total = self.current_total
      #print self.line_total 

      #self.cart.update() # update cart

    #def save(self, *args, **kwargs):
      #super(BaseCartItem, self).save(*args, **kwargs)
      #self.update()

    class Meta(object):
      abstract = True
      app_label = 'cart'
      verbose_name = _('Cart item')
      verbose_name_plural = _('Cart items')