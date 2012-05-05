# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.db import models, transaction
from django.db.models.aggregates import Count

#==============================================================================
# Product
#==============================================================================
class ProductStatisticsManager(models.Manager):
    """
    A Manager for all the non-object manipulation needs, mostly statistics and
    other "data-mining" toys.
    """

    def top_selling_products(self, quantity):
        """
        This method "mines" the previously passed orders, and gets a list of
        products (of a size equal to the quantity parameter), ordered by how
        many times they have been purchased.
        """
        # Importing here is fugly, but it saves us from circular imports...
        from shop.models.ordermodel import OrderItem
        # Get an aggregate of product references and their respective counts
        top_products_data = OrderItem.objects.values(
                'product').annotate(
                    product_count=Count('product')
                ).order_by('product_count'
            )[:quantity]

        # The top_products_data result should be in the form:
        # [{'product_reference': '<product_id>', 'product_count': <count>}, ..]

        top_products_list = []  # The actual list of products
        for values in top_products_data:
            prod = values.get('product')
            # We could eventually return the count easily here, if needed.
            top_products_list.append(prod)

        return top_products_list


class ProductManager(models.Manager):
    """
    A more classic manager for Product filtering and manipulation.
    """
    def active(self):
        return self.filter(active=True)