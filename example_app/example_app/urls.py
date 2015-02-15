from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example_app.views.home', name='home'),

    url(r'^taggit/', include('taggit_selectize.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
