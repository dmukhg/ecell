#!/usr/bin/python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/usr/lib/python2.5/django")
sys.path.insert(0, "/home/caesar/code/ecell2")

# Switch to the directory of your project. (Optional.)
os.chdir("/home/caesar/code/ecell2")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "ecell2.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
~                                                              
