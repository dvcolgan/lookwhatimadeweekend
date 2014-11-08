from django.conf.urls import patterns, url
from contests import views

urlpatterns = patterns('contests.views',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^guidelines/$', views.GuidelinesView.as_view(), name='guidelines'),
    url(r'^contest/(?P<number>\d+)/$', views.ContestDetailView.as_view(), name='contest_detail'),
    url(r'^contest/(?P<number>\d+)/submission/(?P<user_id>\d+)/$', 'submission_detail', name='submission_detail'),
    url(r'^contest/(?P<number>\d+)/submission/edit/$', 'submission_edit', name='submission_edit'),

    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^irc/$', views.IRCView.as_view(), name='irc'),
)
