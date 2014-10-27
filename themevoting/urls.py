from django.conf.urls import patterns, url
from themevoting.views import (
    ThemeBumpView,
    ThemeCreateView,
)

urlpatterns = patterns('themevoting.views',
    url(r'^$', 'theme_dispatch', name='theme_dispatch'),
    url(r'^bump/$', ThemeBumpView.as_view(), name='theme_bump'),
    url(r'^bump/(?P<pk>\d+)/(?P<direction>up|down)/$', 'theme_bump_submit', name='theme_bump_submit'),
    url(r'^suggest/$', ThemeCreateView.as_view(), name='theme_create'),
    url(r'^vote/$', 'theme_vote_view', name='theme_vote'),
    url(r'^vote-submit/$', 'theme_vote_submit_view', name='theme_vote_submit'), )
