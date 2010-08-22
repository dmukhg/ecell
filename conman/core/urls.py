from django.conf.urls.defaults import *
from ecell2 import settings
from ecell2.conman.core.views import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^$', home),
     (r'^workshop',pre_reg_entry ),
     (r'^custom_view',custom_view ),
     (r'^page/(?P<url>.*)/?$', pages ),
     (r'^(?P<url>.*)/?$', article),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
