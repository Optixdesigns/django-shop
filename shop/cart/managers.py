from django.db import models

class CartManager(models.Manager):
  def get_for_request(self, request):
    if request.user.is_authenticated():
      return self.get_or_create(user=request.user)[0]
    
    if 'cart' in request.session:
      try:
        return self.get(pk=request.session['cart'])
      except self.model.DoesNotExist:
        pass
    
    cart = self.create(user=None)
    request.session['cart'] = cart.pk
    return cart