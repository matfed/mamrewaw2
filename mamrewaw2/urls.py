from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/events/'}),
    url(r'^events/$', 'events.views.index'),
    url(r'^events/archive/$', 'events.views.archive'),
    url(r'^events/(?P<event_id>\d+)/$', 'events.views.detail'),
    url(r'^events/locations/$', 'events.views.locations'),
    url(r'^ballot/landing/(?P<token>[a-f0-9]+)/', 'ballot.views.landing'),
    url(r'^ballot/check/', 'ballot.views.check'),
    url(r'^ballot/confirm/', 'ballot.views.confirm'),
    url(r'^ballot/finish/', 'ballot.views.finish'),
    # Examples:
    # url(r'^$', 'mamrewaw2.views.home', name='home'),
    # url(r'^mamrewaw2/', include('mamrewaw2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
