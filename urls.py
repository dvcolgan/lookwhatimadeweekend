from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('lwimw.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^account/password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^account/password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^account/password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^account/password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^account/complete-reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^account/complete-reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
)
