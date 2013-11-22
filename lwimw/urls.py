from django.conf.urls import patterns, include, url
from django.conf import settings
from lwimw.models import *
from lwimw.views import *

urlpatterns = patterns('lwimw.views',
    url(r'^$', 'home', name='home'),
    url(r'^guidelines/$', 'guidelines', name='guidelines'),
    url(r'^accounts/profile/$', 'profile', name='profile'),
    url(r'^contest/(?P<number>\d+)/$', 'submissions_list', name='submissions_list'),
    url(r'^contest/(?P<number>\d+)/submission/(?P<user_id>\d+)/$', 'submission_detail', name='submission_detail'),
    url(r'^contest/(?P<number>\d+)/submission/edit/$', 'submission_edit', name='submission_edit'),

    url(r'^posts/create/$', 'post_create', name='post_create'),
    url(r'^posts/(?P<post_id>\d+)/edit/$', 'post_edit', name='post_edit'),

    url(r'^profile/$', 'profile', name='profile'),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name='profile'),
    url(r'^irc/$', 'irc', name='irc'),
)
