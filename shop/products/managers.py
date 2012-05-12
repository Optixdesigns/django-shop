# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.db import models, transaction
from django.db.models.aggregates import Count
from polymorphic.manager import PolymorphicManager

#==============================================================================
# Product
#==============================================================================
class ProductStatisticsManager(models.Manager):
    """
    A Manager for all the non-object manipulation needs, mostly statistics and
    other "data-mining" toys.
    """

    def top_selling_products(self, quantity):
        pass


class ProductManager(models.Manager):
    pass