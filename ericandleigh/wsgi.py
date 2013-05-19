import os
import sys
sys.path.append('/var/django/ericandleigh.com')
sys.path.append('/var/django')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()