from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="intro.html")),
    url(r'^events/$', TemplateView.as_view(template_name="intro.html")),
    url(r'^events/calendar/$', 'events.views.index'),
    url(r'^events/calendar/archive/$', 'events.views.archive'),
    url(r'^events/calendar/(?P<event_id>\d+)/$', 'events.views.detail'),
    url(r'^events/locations/$', 'events.views.locations'),
    url(r'^events/blog/$', 'blog.views.index'),
    url(r'^events/blog/(?P<post_id>\d+)/$', 'blog.views.post'),
    # Examples:
    # url(r'^$', 'mamrewaw2.views.home', name='home'),
    # url(r'^mamrewaw2/', include('mamrewaw2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
