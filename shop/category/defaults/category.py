from django.core.urlresolvers import reverse
from django.db import models
from hub.categories.bases import CategoryBase

class Category(CategoryBase):
  class Meta:
    abstract = False
    app_label = 'categories'
    ordering            = ('name',)
    verbose_name        = 'category'
    verbose_name_plural = 'categories'

  def get_absolute_url(self):
      return reverse('category_object_list', kwargs={'category_slug': self.slug})