from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'utils.direct_to_template', {'template': 'index.html'}),
    url(r'^events/$', 'events.views.index'),
    url(r'^events/archive/$', 'events.views.archive'),
    url(r'^events/(?P<event_id>\d+)/$', 'events.views.detail'),
    url(r'^events/locations/$', 'events.views.locations'),
    url(r'^regulations/$', 'utils.direct_to_template', {'template': 'regulations.html'}),
    # Examples:
    # url(r'^$', 'mamrewaw2.views.home', name='home'),
    # url(r'^mamrewaw2/', include('mamrewaw2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
