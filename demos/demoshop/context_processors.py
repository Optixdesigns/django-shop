from django.conf import settings

def site_settings(request):
    site_settings_dict = {
      'LANGUAGE_CODE': settings.LANGUAGE_CODE,
      'SITE_NAME': settings.SITE_NAME,
      'POWERED_BY': settings.POWERED_BY,
      'POWERED_BY_EMAIL': settings.POWERED_BY_EMAIL,
      'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
    }
    return site_settings_dict