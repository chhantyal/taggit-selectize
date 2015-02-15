# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns('',
    url('^$', 'get_tags_recommendation', name='tags_recommendation'),
)