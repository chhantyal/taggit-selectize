import json

from django.http import HttpResponse
from django.utils.module_loading import import_string
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

    try:
        cls = import_string(settings.TAGGIT_SELECTIZE_THROUGH)
    except AttributeError:
        cls = Tag

    if query:
        tags = cls.objects.filter(name__icontains=query).values('name')[:limit]
    else:
        tags = cls.objects.values()[:limit]

    data = json.dumps({
        'tags': list(tags)
    })

    return HttpResponse(data, content_type='application/json')
