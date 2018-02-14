taggit-selectize
================

Auto-complete/auto-suggestion for django-taggit.

[django-taggit](https://github.com/alex/django-taggit) + [selectize.js](https://github.com/brianreavis/selectize.js)

![taggit-selectize demo screenshot](https://i.imgur.com/ryxW6TI.png)

With `django-taggit`, you can attach tags in any Django models. However, user experience is not that good as it uses
comma to separate multiple tags in same form field, and resulting in duplicate tags eg. Himalaya vs. Himalayas, Sublime-Text vs. Sublime Text etc.
And you probably want auto-complete/auto-suggest feature when user types some characters in tag field. Thanks to selectize.js, we got that covered :)


Features
--------
* Supports Django 1.8.x and Django 1.9.x
* Supports >=Python2.7 and >=Python3.4
* Simple installation, selectize.js 0.12.1 included
* Will use jQuery install included in Django admin, no installation of jQuery needed
* Will use custom jQuery object if it is installed, though
* Themed to match new Django 1.9 flat theme
* Exposes many selectize.js configuration options to your settings.py
* Supports multiple TaggableManagers in a single model


Quickstart
----------

Install taggit-selectize:
```bash
pip install taggit-selectize
```

Usage
-----

1. Put `taggit_selectize` in settings:
    ```python
    INSTALLED_APPS = (
        'django.contrib.admin',
        ...
        ...
        'taggit',
        'taggit_selectize',
    )
    ```

2. Configured Taggit in your Django settings to use a custom string-to-tag parser that doesn't parse on spaces to match the functionality of
Selectize.js, and a custom tag joiner that supports configurable delimiters.
    ```python
    TAGGIT_TAGS_FROM_STRING = 'taggit_selectize.utils.parse_tags'
    TAGGIT_STRING_FROM_TAGS = 'taggit_selectize.utils.join_tags'
    ```

3. Update urls.py.
    ```python
    urlpatterns = [
        ...
    
        url(r'^taggit/', include('taggit_selectize.urls')),
        url(r'^admin/', include(admin.site.urls)),
        ...
    ]
    ```

4. Use the `TaggableManager` from taggit_selectize (instead of taggit) in your models.
    ```python
    from taggit_selectize.managers import TaggableManager
    
    class MyModel(models.Model):
        tags = TaggableManager()
    ```


Configuration
-------------
In your settings.py (these are defaults):

```python
TAGGIT_SELECTIZE = {
    'MINIMUM_QUERY_LENGTH': 2,
    'RECOMMENDATION_LIMIT': 10,
    'CSS_FILENAMES': ("taggit_selectize/css/selectize.django.css",),
    'JS_FILENAMES': ("taggit_selectize/js/selectize.js",),
    'DIACRITICS': True,
    'CREATE': True,
    'PERSIST': True,
    'OPEN_ON_FOCUS': True,
    'HIDE_SELECTED': True,
    'CLOSE_AFTER_SELECT': False,
    'LOAD_THROTTLE': 300,
    'PRELOAD': False,
    'ADD_PRECEDENCE': False,
    'SELECT_ON_TAB': False,
    'REMOVE_BUTTON': False,
    'RESTORE_ON_BACKSPACE': False,
    'DRAG_DROP': False,
    'DELIMITER': ','
}
```

### MINIMUM_QUERY_LENGTH

The minimum number of characters the user needs to type to cause an AJAX request to hit the server for autocompletion. Default: 2

### RECOMMENDATION_LIMIT

The maximum number of results to return to the user for recommendation. Default: 10

### CSS_FILENAMES

A tuple of CSS files to include on any page that has the taggit-selectize widget on it. Default: `("taggit_selectize/css/selectize.django.css",)`

### JS_FILENAMES

A tuple of JS files to include on any page that has the taggit-selectize widget on it. Default: `("taggit_selectize/js/selectize.js",)`

### DIACRITICS, CREATE, PERSIST, OPEN_ON_FOCUS, HIDE_SELECTED, CLOSE_AFTER_SELECT, LOAD_THROTTLE, PRELOAD, ADD_PRECEDENCE, SELECT_ON_TAB

Options that are passed directly to selectize.js.
Please see [the selectize.js documentation](https://github.com/selectize/selectize.js/blob/master/docs/usage.md) for explanation

### REMOVE_BUTTON

Adds a remove button to each tag item by including the 'remove_button' plugin.

### RESTORE_ON_BACKSPACE

Adds the 'restore_on_backspace' plugin to selectize.js.

### DRAG_DROP

Adds the 'drag_drop' plugin to selectize.js. WARNING: This requires JQuery UI (Sortable) to be installed. If it's not, then
selectize.js will throw an error in the console and refuse to run.

### DELIMITER

Set the delimiter between tags, for example, ';' or '|'. Make sure you have set up the custom TAGGIT_STRING_FROM_TAGS for this to work properly
with Taggit. Default is comma, ','.

Demo app
--------

There is demo app included `example_app`.

1. `cd example_app`
2. `python manage.py migrate`
3. `python manage.py runserver`

Login username: `admin` password: `admin`


Versions
--------
1. 0.x Initial release with Django 1.5 - 1.8 support. Latest upload on this series is `0.1.2`. Use this if you need old Django support.

2. 1.x Release with Django 1.9 support.

3. 2.x This version might introduce backward incompatibility. It improves the way it works (widget instead of admin overrride) and adds many new features 
[Thanks a ton to Nathan](https://github.com/chhantyal/taggit-selectize/pull/5).
