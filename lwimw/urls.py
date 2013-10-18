from django.conf.urls import patterns, include, url
from django.conf import settings
from lwimw.models import *
from lwimw.views import *

urlpatterns = patterns('lwimw.views',
    url(r'^$', 'home', name='home'),
    url(r'^guidelines/$', 'guidelines', name='guidelines'),
    url(r'^accounts/profile/$', 'profile', name='profile'),
    url(r'^contest/(?P<number>\d+)/$', 'submissions_list', name='submissions_list'),
    url(r'^contest/(?P<number>\d+)/submission/(?P<user_id>\d+)/$', 'submission', name='submission'),
    #url(r'^settings/$', 'settings', name='settings'),
    url(r'^irc/$', 'irc', name='irc'),
)


