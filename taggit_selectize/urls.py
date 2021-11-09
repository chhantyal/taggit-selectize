from django.urls import path

from .views import get_tags_recommendation

urlpatterns = [
    path('', get_tags_recommendation, name='tags_recommendation'),
]
