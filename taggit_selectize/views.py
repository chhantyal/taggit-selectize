# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse

from taggit.models import Tag

from taggit_selectize.conf import settings


def get_tags_recommendation(request):
    """
    Taggit autocomplete ajax view.
    Response objects are filtered based on query param.
    Tags are by default limited to 10, use TAGGIT_SELECTIZE_RECOMMENDATION_LIMIT settings to specify.
    """
    query = request.GET.get('query')
    if query:
        limit = settings.TAGGIT_SELECTIZE_RECOMMENDATION_LIMIT
        recommended_tags = Tag.objects.filter(name__icontains=query).values('name')[:limit]
        tags = list(recommended_tags)
    else:
        tags = list(Tag.objects.values()[:10])

    data = json.dumps({
        'tags': tags
    })

    return HttpResponse(data, content_type='application/json')