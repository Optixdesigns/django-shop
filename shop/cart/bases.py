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

    def __init__(self, *args, **kwargs):
        # That will hold extra fields to display to the user
        # (ex. taxes, discount)
        super(BaseCartItem, self).__init__(*args, **kwargs)
        self.extra_price_fields = []  # list of tuples (label, value)
        # These must not be stored, since their components can be changed
        # between sessions / logins etc...
        self.line_subtotal = Decimal('0.0')
        self.line_total = Decimal('0.0')
        self.current_total = Decimal('0.0')  # Used by cart modifiers

    def update(self, state):
        self.extra_price_fields = []  # Reset the price fields
        self.line_subtotal = self.product.get_price() * self.quantity
        self.current_total = self.line_subtotal

        for modifier in cart_modifiers_pool.get_modifiers_list():
            # We now loop over every registered price modifier,
            # most of them will simply add a field to extra_payment_fields
            modifier.process_cart_item(self, state)

        self.line_total = self.current_total
        return self.line_total