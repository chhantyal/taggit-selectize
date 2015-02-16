=============================
taggit-selectize
=============================

Auto-complete/auto-suggestion for django-taggit.

[django-taggit](https://github.com/alex/django-taggit) + [selectize.js](https://github.com/brianreavis/selectize.js)

![taggit-selectize demo screenshot](https://i.imgur.com/ryxW6TI.png)

With `django-taggit`, you can attach tags in any Django models. However, user experience is not that good as it uses
comma to separate multiple tags in same form field, and resulting in duplicate tags eg. Himalaya vs. Himalayas, Sublime-Text vs. Sublime Text etc.
And you probably want auto-complete/auto-suggest feature when user types some characters in tag field. Thanks to selectize.js, we got that covered :)


Quickstart
----------

Install taggit-selectize::

    pip install taggit-selectize


Usage
-----

1. Put `taggit-selectize` in settings:

```
INSTALLED_APPS = (
    'django.contrib.admin',
    ...
    ...
    'taggit_selectize',
)
```

2. Update urls.py.
```
urlpatterns = patterns('',
    ...

    url(r'^taggit/', include('taggit_selectize.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ...
)
```

3. Create `admin` dir inside templates folder. Create a template `base_site.html` and [copy paste this](https://github.com/chhantyal/taggit-selectize/blob/master/example_app/templates/admin/base_site.html).
This has to override from project template dirs otherwise django will still load default `base_site.html` from `django.contrib.admin` app.
Also, filesystem loader must be before app dir loader in settings like:

```
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
```
You can also use outside of admin in same way.


Demo app
--------

There is demo app included `example_app`.

1. `cd example_app`
2. `python manage.py migrate`
3. `python manage.py runserver`

Login username: `admin` password: `admin`
