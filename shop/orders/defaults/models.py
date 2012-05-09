# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from shop.utils.fields import CurrencyField
from django.contrib.auth.models import User

class BaseOrder(models.Model):
    """
    A model representing an Order.

    An order is the "in process" counterpart of the shopping cart, which holds
    stuff like the shipping and billing addresses (copied from the User
    profile) when the Order is first created), list of items, and holds stuff
    like the status, shipping costs, taxes, etc...
    """

    PROCESSING = 1  # New order, no shipping/payment backend chosen yet
    PAYMENT = 2  # The user is filling in payment information
    CONFIRMED = 3  # Chosen shipping/payment backend, processing payment
    COMPLETED = 4  # Successful payment confirmed by payment backend
    SHIPPED = 5  # successful order shipped to client
    CANCELLED = 6  # order has been cancelled

    STATUS_CODES = (
        (PROCESSING, _('Processing')),
        (PAYMENT, _('Selecting payment')),
        (CONFIRMED, _('Confirmed')),
        (COMPLETED, _('Completed')),
        (SHIPPED, _('Shipped')),
        (CANCELLED, _('Cancelled')),
    )

    # If the user is null, the order was created with a session
    user = models.ForeignKey(User, blank=True, null=True, verbose_name=_('User'))
    status = models.IntegerField(choices=STATUS_CODES, default=PROCESSING, verbose_name=_('Status'))
    order_subtotal = CurrencyField(verbose_name=_('Order subtotal'))
    order_total = CurrencyField(verbose_name=_('Order Total'))
    shipping_address_text = models.TextField(_('Shipping address'), blank=True, null=True)
    billing_address_text = models.TextField(_('Billing address'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    modified = models.DateTimeField(auto_now=True,verbose_name=_('Updated'))

    class Meta(object):
        abstract = True
        app_label = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

class Order(BaseOrder):
    class Meta(object):
        abstract = False
        app_label = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        db_table = 'shop_orders_order'