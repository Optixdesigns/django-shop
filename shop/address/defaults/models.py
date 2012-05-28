# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user_shipping = models.OneToOneField(User, related_name='shipping_address', blank=True, null=True)
    user_billing = models.OneToOneField(User, related_name='billing_address', blank=True, null=True)
    name = models.CharField(_('Name'), max_length=255)
    address = models.CharField(_('Address'), max_length=255)
    address2 = models.CharField(_('Address2'), max_length=255, blank=True)
    zip_code = models.CharField(_('Zip Code'), max_length=20)
    city = models.CharField(_('City'), max_length=20)
    state = models.CharField(_('State'), max_length=255)
    country = models.ForeignKey(Country, verbose_name=_('Country'), blank=True, null=True)
    
    class Meta(object):
        app_label = 'addresses'
        db_table = 'shop_addresses_address'
        verbose_name = _('Address')
        verbose_name_plural = _("Addresses")

    def __unicode__(self):
        return '%s (%s, %s)' % (self.name, self.zip_code, self.city)

    def clone(self):
        new_kwargs = dict([(fld.name, getattr(self, fld.name))
                           for fld in self._meta.fields if fld.name != 'id'])
        return self.__class__.objects.create(**new_kwargs)

    def as_text(self):
        return ADDRESS_TEMPLATE % {
            'name': self.name,
            'address': '%s\n%s' % (self.address, self.address2),
            'zipcode': self.zip_code,
            'city': self.city,
            'state': self.state,
            'country': self.country,
        }