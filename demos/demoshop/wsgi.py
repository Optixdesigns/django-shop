import os
import sys
import site

#PATH = '/usr/local/projects/shop'
PATH = '/home/sarendsen/webapps/exampleshop/myproject'

# Virtualenv
#site.addsitedir('%s/env/lib/python2.6/site-packages' % PATH)
site.addsitedir('%s/shared/venv/lib/python2.7/site-packages' % PATH)
site.addsitedir('%s/current/exampleshop/apps/' % PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'exampleshop.settings'

activate_this = os.path.expanduser('%s/shared/venv/bin/activate_this.py' % PATH)
execfile(activate_this, dict(__file__=activate_this))

project = '%s/current/exampleshop/' % PATH
workspace = os.path.dirname(project)
sys.path.append(workspace)

# Django 1.4
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()