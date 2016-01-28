from django.utils.text import capfirst
from taggit.forms import TagField
from taggit.managers import TaggableManager as BaseTaggableManager
from .widgets import TagSelectize


class TaggableManager(BaseTaggableManager):
    def formfield(self, form_class=TagField, **kwargs):
        defaults = {
            "label": capfirst(self.verbose_name),
            "help_text": None,
            "required": not self.blank,
            "widget": TagSelectize,
        }
        defaults.update(kwargs)
        return form_class(**defaults)
