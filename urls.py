from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('lwimw.urls')),
    url(r'themes/', include('themevoting.urls')),
    url(r'^posts/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^account/password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^account/password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^account/password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^account/password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^account/complete-reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
