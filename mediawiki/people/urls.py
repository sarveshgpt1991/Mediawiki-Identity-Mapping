from django.conf.urls import patterns, include, url

urlpatterns = patterns('people.views',

    url(r'^$', 'home'),
)
