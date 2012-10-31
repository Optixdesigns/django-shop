from django.db import models
from django.contrib.auth.models import User
from collector.models import ProfileBase
from datetime import *

class Profile(ProfileBase):
  first_name  = models.CharField(max_length=200, blank=True, null=True)
  last_name  = models.CharField(max_length=200, blank=True, null=True)
  preposition  = models.CharField(max_length=20, blank=True, null=True)
  phone_number = models.CharField(max_length=20, blank=True, null=True)
  birthday     = models.DateField(blank=True, null=True)
  gender       = models.CharField(max_length=20, blank=True, null=True, choices=(('M', 'Man'),('F', 'Vrouw'),))

  class Meta:
    verbose_name = 'basic profile'
    verbose_name_plural = 'Basic Profiles'