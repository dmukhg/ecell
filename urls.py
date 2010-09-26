from django.conf.urls.defaults import *
from django.views.static import serve as stat
from ecell2 import settings, root_views

# Uncomment the next two lines to enable the admin:
#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^account/', include('ecell2.account.urls')),
    (r'^upload/' , include('ecell2.upload.urls')),
    (r'^$', include('ecell2.conman.core.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin$', root_views.go ), 
    #(r'^admin/', include(admin.site.urls)),
    (r'^admin/?', include('ecell2.conman.admin.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
            (r'^site_media/(?P<path>.*)$', stat,{'document_root': '/home/caesar/code/ecell2/site_media'}),
	)

urlpatterns += patterns('',
    (r'^edit',include('ecell2.conman.edit.urls')),
    (r'', include('ecell2.conman.core.urls')),
)
