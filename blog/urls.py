from django.conf.urls import patterns, include, url
from django.conf import settings
from blog.models import *
from blog.views import *

urlpatterns = patterns('blog.views',
    url(r'^create/$', 'post_create', name='post_create'),
    url(r'^comment/reply/$', 'comment_reply', name='comment_reply'),
    url(r'^comment/delete/$', 'comment_delete', name='comment_delete'),
    url(r'^(?P<post_id>\d+)/edit/$', 'post_edit', name='post_edit'),
    url(r'^(?P<post_id>\d+)/$', 'post_detail', name='post_detail')
)
