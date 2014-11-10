from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/events/calendar/'}),
    url(r'^events/calendar/$', 'events.views.index'),
    url(r'^events/calendar/archive/$', 'events.views.archive'),
    url(r'^events/calendar/(?P<event_id>\d+)/$', 'events.views.detail'),
    url(r'^events/locations/$', 'events.views.locations'),
    # Examples:
    # url(r'^$', 'mamrewaw2.views.home', name='home'),
    # url(r'^mamrewaw2/', include('mamrewaw2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
