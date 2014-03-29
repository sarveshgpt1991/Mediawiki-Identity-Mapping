from django.conf.urls import patterns, include, url

urlpatterns = patterns('people.views',

    url(r'^$', 'home'),
    url(r'^/add/(?P<identifier>(name)|(country)|(email))$', 'addIdentity'),
    url(r'^/remove/(?P<identifier>(name)|(country)|(email))/(?P<Id>[0-9]+)', "removeIdentity")

)
