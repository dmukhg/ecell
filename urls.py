from django.conf.urls.defaults import *
from django.views.static import serve as stat
from ecell2 import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^account/', include('ecell2.account.urls')),
    (r'^article/', include('ecell2.conman.urls')),
    (r'^$', include('ecell2.conman.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
            (r'^site_media/(?P<path>.*)$', stat,{'document_root': '/home/caesar/code/ecell2/site_media'}),
	)
