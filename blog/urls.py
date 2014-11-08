from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('blog.views',
    url(r'^create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^delete/$', 'post_delete', name='post_delete'),
    url(r'^(?P<post_id>\d+)/edit/$', 'post_edit', name='post_edit'),
    url(r'^(?P<post_id>\d+)/$', 'post_detail', name='post_detail'),
    url(r'^comment/reply/$', 'comment_reply', name='comment_reply'),
    url(r'^comment/delete/$', 'comment_delete', name='comment_delete'),
)
