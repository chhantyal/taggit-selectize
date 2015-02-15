# -*- coding: utf-8 -*-

from django.conf import settings

settings.TAGGIT_SELECTIZE_RECOMMENDATION_LIMIT = getattr(settings,
    'TAGGIT_SELECTIZE_RECOMMENDATION_LIMIT', 10
)