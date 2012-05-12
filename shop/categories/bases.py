from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager

class CategoryBase(MPTTModel):
  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)
  name        = models.CharField(max_length=200, help_text='Short descriptive name for this category.',)
  description = models.TextField(blank=True, null=True)
  slug        = AutoSlugField(populate_from='name', max_length=255, editable=True, blank=True, help_text='Short descriptive unique name for use in urls.',)
  plural      = models.CharField(max_length=255, blank=True)
  parent      = TreeForeignKey('self', null=True, blank=True, related_name='children')
  
  tree = TreeManager()

  class Meta:
    abstract = True
    ordering            = ('name',)
    verbose_name        = 'category'
    verbose_name_plural = 'categories'
  
  def __unicode__(self):
    return self.name
  
  class MPTTMeta:
    order_insertion_by=['name']