from django.utils.translation import ugettext_lazy as _
from shop.category.bases import CategoryBase
from django.core.urlresolvers import reverse
from django.db import models

class ProductCategory(CategoryBase):
  class Meta:
    ordering            = ('name',)
    verbose_name        = 'category'
    verbose_name_plural = 'categories'

  def get_absolute_url(self):
    return reverse('shop_catalog', kwargs={'category_slug': self.slug})