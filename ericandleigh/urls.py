from django.conf.urls import patterns, include, url
from django.conf import settings
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name = "home"),
	url(r'^(?i)theproposal$', views.theproposal, name = "Proposal"),
	url(r'^(?i)ourstory$', views.ourstory, name = "Story"),
	url(r'^(?i)rsvp$', views.rsvp, name = "RSVP"),
	url(r'^(?i)registry$', views.registry, name = "Registry"),
	url(r'^(?i)weddingevents$', views.weddingevents, name = "Events"),
	url(r'^(?i)weddingparty$', views.weddingparty, name = "Party"),
	url(r'^(?i)photos$', views.photos, name = "Photos"),
	#url(r'^(?P<item>[a-zA-Z]+)$', views.stuff, name = "stuff"),
)

if settings.DEBUG :
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT } )
    )
