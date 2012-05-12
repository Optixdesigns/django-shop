# -*- coding: utf-8 -*-
from shop.cart.models import Cart
from shop.categories.models import Category

class ShopApi(object):
	def __init__(self, request, *args, **kwargs):
		self.request = request
		self.cart = Cart.objects.get_for_request(self.request) 
		super(ShopApi, self).__init__(*args, **kwargs)

	def categories(self): 
		return Category.objects.all()