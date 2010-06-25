from django.conf.urls.defaults import *
from ecell2 import settings
from ecell2.conman.admin_views import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^$', index ),
    
    # updates related
     (r'^updates/add$' , updates_add),
     (r'^updates/edit/(?P<pk>\d+)$' , updates_add),
     (r'^updates/delete/(?P<pk>\d+)$', updates_delete ),

    # sector related
     (r'^sector/add$' , sector_add),
     (r'^sector/edit/(?P<pk>\d+)$' , sector_add),
    # (r'^updates/delete/(?P<pk>\d+)$', updates_delete ),

   # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
