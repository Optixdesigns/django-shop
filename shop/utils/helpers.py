#-*- coding: utf-8 -*-
from django.conf import settings
from django.core import exceptions
from django.utils.importlib import import_module

def get_model_string(model_name):
    setting_name = 'SHOP_%s_MODEL' % model_name.upper().replace('_', '')
    class_path = getattr(settings, setting_name, None)
        
    if not class_path:
        return model_name
    elif isinstance(class_path, basestring):
        parts = class_path.split('.')
        try:
            index = parts.index('models') - 1
        except ValueError, e:
            raise exceptions.ImproperlyConfigured(CLASS_PATH_ERROR % (setting_name, setting_name))
        app_label, model_name = parts[index], parts[-1]
    else:
        try:
            class_path, app_label = class_path
            model_name = class_path.split('.')[-1]
        except:
            raise exceptions.ImproperlyConfigured(CLASS_PATH_ERROR % (setting_name, setting_name))

    return "%s.%s" % (app_label, model_name)