#!/usr/bin/env python
import sys
import warnings

from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'taggit_selectize',
            'taggit',
            'tests',
        ],
        MIDDLEWARE_CLASSES=[],
        ROOT_URLCONF='taggit_selectize.urls',
    )


warnings.simplefilter('default', DeprecationWarning)
warnings.simplefilter('default', PendingDeprecationWarning)


def runtests():
    argv = sys.argv[:1] + ['test'] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()
