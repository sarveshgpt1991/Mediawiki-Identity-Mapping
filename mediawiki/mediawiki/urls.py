from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #login, signup
    url(r'^$', 'login.views.home', name='home'),
    url(r'^signup$', 'login.views.signup'),
    url(r'^signin$', 'login.views.signin'),
    url(r'^logout$', 'login.views.signout'),
    
    #user-specific
    #url(r'signup/set_password/$', 'login.views.set_password'),
    #url(r'^(?P<user_name>\w+)/', include('users.urls')),

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
