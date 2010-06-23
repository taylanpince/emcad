import os
import sys
import site

site.addsitedir('/home/emcadteam/sites/emcad/lib/python2.6/site-packages')

sys.path.append("/home/emcadteam/sites/emcad/src/emcad/build")
sys.path.append("/home/emcadteam/sites/emcad/src/emcad/build/emcad")

os.environ["DJANGO_SETTINGS_MODULE"] = "emcad.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
