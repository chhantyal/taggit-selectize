import json

from django.http import HttpResponse

from taggit.models import Tag
from .conf import settings


def get_tags_recommendation(request):
    """
    Taggit autocomplete ajax view.
    Response objects are filtered based on query param.
    Tags are by default limited to 10, use TAGGIT_SELECTIZE_RECOMMENDATION_LIMIT settings to specify.
    """
    query = request.GET.get('query')
    limit = settings.TAGGIT_SELECTIZE['RECOMMENDATION_LIMIT']
    if query:
        tags = Tag.objects.filter(name__icontains=query).values('name')[:limit]
    else:
        tags = Tag.objects.values()[:limit]

    data = json.dumps({
        'tags': list(tags)
    })

    return HttpResponse(data, content_type='application/json')
