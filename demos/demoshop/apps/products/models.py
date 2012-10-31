from django.utils.translation import ugettext_lazy as _
from shop.category.bases import CategoryBase
from shop.product.bases import BaseProduct, VariantBase
from shop.contrib.stock.models import VariantStockLevelMixin
from hub.core.models import Featurable, Displayable, Orderable, RichText
from sorl.thumbnail import ImageField
from django.db import models
#from nuggets.models import Nugget
#from shop.categories.models import Category
from shop.utils.helpers import get_model_string
import decimal
import os

class Product(BaseProduct, Displayable, Featurable, RichText):
  '''
  Base product model
  '''
  categories = models.ManyToManyField(get_model_string('Category'))

  class Meta:
    abstract = False
    #app_label = 'Shop'
    verbose_name = _('Product')
    verbose_name_plural = _('Products')

class Variant(VariantBase, VariantStockLevelMixin):
  '''
  Base variant model
  '''

  #product = models.ForeignKey(Product, related_name='variants')
  price_offset = models.DecimalField(_("unit price offset"), default=decimal.Decimal(0),  max_digits=12, decimal_places=4)

  class Meta:
    abstract = False

class SimpleProduct(Product, VariantStockLevelMixin):
  '''
  A simple product
  '''
  class Meta:
    abstract = False
    verbose_name = _('Simple Product')
    verbose_name_plural = _('Simple Products')

class Poster(Product):
  '''
  Poster product type
  '''
  class Meta:
    abstract = False
    verbose_name = _('Poster')
    verbose_name_plural = _('Poster')

  def get_variant_model(self):
    return PosterVariant

class Clothing(Product):
  '''
  Poster product type
  '''
  class Meta:
    abstract = False
    verbose_name = _('Clothing')
    verbose_name_plural = _('Clothing')

  def get_variant_model(self):
    return ClothingVariant  

class Ticket(Product):
  '''
  Ticket product type
  '''
  class Meta:
    abstract = False
    verbose_name = _('Ticket')
    verbose_name_plural = _('Ticket')

  def get_variant_model(self):
    return TicketVariant      

class TicketVariant(Variant):
  product = models.ForeignKey(Ticket, related_name='variants')
  RING_CHOICES = (('1', _("1st ring")), ('2', _("2th ring")), ('outer', _("Outer ring")))
  ring = models.CharField(max_length=255, choices=RING_CHOICES, blank=False)

  def form_fields(self):
    return ['ring',]

class PosterVariant(Variant):
  product = models.ForeignKey(Poster, related_name='variants')
  FRAME_CHOICES = (('unframed', _("Unframed")), ('black', _("Black Frame")),)
  frame = models.CharField(max_length=255, choices=FRAME_CHOICES, blank=False)
  SIZE_CHOICES = (('30x22', '30 x 22'), ('20x30', '20 x 30'),)
  size = models.CharField(choices=SIZE_CHOICES, max_length=255, blank=False)

  def form_fields(self):
    return ['frame', 'size',]

class ClothingVariant(Variant):
  product = models.ForeignKey(Clothing, related_name='variants')
  COLOR_CHOICES = (('red', _("Red")), ('blue', _("Blue")), ('green', _("Green")), ('yellow', _("Yellow")), ('purple', _("Purple")), )
  frame = models.CharField(max_length=255, choices=COLOR_CHOICES, blank=False)
  SIZE_CHOICES = (('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'),)
  size = models.CharField(choices=SIZE_CHOICES, max_length=255, blank=False)

  def form_fields(self):
    return ['frame', 'size',]

class ProductImage(models.Model):
  '''
  Product image mixin
  '''
  product = models.ForeignKey(Product, related_name="images")
  image = ImageField(upload_to='products/', blank=True, null=True, default='project/images/no-image.jpg')
  caption = models.CharField(_("Caption"), max_length=128, blank=True)
  weight = models.PositiveIntegerField(blank=True, default=0)

  class Meta:
      ordering = ('weight',)

  def __unicode__(self):
      return os.path.basename(self.image.name)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^hub\.core\.fields\.RichTextField"])