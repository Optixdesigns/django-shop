from django.utils.functional import SimpleLazyObject
from shop.cart.models import Cart
from shop.categories.models import Category
from shop.api import ShopApi

class ShopMiddleware(object):
  def process_request(self, request):
    request.shop = ShopApi(request)