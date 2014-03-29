from django.conf.urls import patterns, include, url
from mediawiki.settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #login, signup
    url(r'^$', 'login.views.home', name='home'),
    url(r'^signup$', 'login.views.signup'),
    url(r'^signin$', 'login.views.signin'),
    url(r'^signout$', 'login.views.signout'),
    
    #user-specific
    url(r'^(?P<username>\w+)', include('people.urls')),
    #url(r'signup/set_password/$', 'login.views.set_password'),

    #media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
