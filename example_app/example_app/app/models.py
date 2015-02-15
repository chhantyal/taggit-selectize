# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=True, max_length=255, unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title