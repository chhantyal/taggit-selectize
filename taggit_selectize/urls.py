from django.conf.urls import *

from .views import get_tags_recommendation

urlpatterns = [
    url(r'^$', get_tags_recommendation, name='selectize_tags_recommendation'),
]
