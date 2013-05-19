import os
sys.path.append('/var/django/ericandleigh.com')
sys.path.append('/var/django')

os.environ.setdefault("DJANGO_  SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()