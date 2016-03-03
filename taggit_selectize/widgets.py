from django import forms
from django.core.urlresolvers import reverse
from django.utils import six
from django.utils.safestring import mark_safe
from taggit.utils import edit_string_for_tags

from .conf import settings


class TagSelectize(forms.TextInput):
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, six.string_types):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
        html = super(TagSelectize, self).render(name, value, attrs)

        js_plugins = []
        if settings.TAGGIT_SELECTIZE['REMOVE_BUTTON']:
            js_plugins.append("remove_button")
        if settings.TAGGIT_SELECTIZE['RESTORE_ON_BACKSPACE']:
            js_plugins.append("restore_on_backspace")
        if settings.TAGGIT_SELECTIZE['DRAG_DROP']:
            js_plugins.append("drag_drop")

        js = u"""
            <script type="text/javascript">
                (function($) {
                    $(document).ready(function() {
                        $("input[id=%(id)s]").selectize({
                            valueField: 'name',
                            labelField: 'name',
                            searchField: 'name',
                            diacritics: %(diacritics)s,
                            create: %(create)s,
                            persist: %(persist)s,
                            openOnFocus: %(open_on_focus)s,
                            hideSelected: %(hide_selected)s,
                            closeAfterSelect: %(close_after_select)s,
                            loadThrottle: %(load_throttle)d,
                            preload: %(preload)s,
                            addPrecedence: %(add_precedence)s,
                            selectOnTab: %(select_on_tab)s,
                            plugins: [%(plugins)s],
                            render: {
                                option: function(item, escape) {
                                    return '<div>' +
                                        '<span class="title">' +
                                            '<span class="name">' + escape(item.name) + '</span>' +
                                        '</span>' +
                                    '</div>';
                                },
                                'item': function(item, escape) {
                                    name = item.name.replace(/^\s*"|"\s*$/g, '');
                                    return '<div class="item">' + escape(name) + '</div>';
                                }
                            },
                            load: function(query, callback) {
                                if (query.length < %(minimum_query_length)d) return callback();
                                $.ajax({
                                    url: '%(remote_url)s?query=' + encodeURIComponent(query),
                                    type: 'GET',
                                    error: function() {
                                        callback();
                                    },
                                    success: function(res) {
                                        callback(res.tags.slice(0, %(recommendation_limit)s));
                                    }
                                });
                            }
                        }).parents('.form-row').css('overflow', 'visible');
                    });
                })(jQuery || django.jQuery);
            </script>
        """ % {
            'id': attrs['id'],
            'minimum_query_length': settings.TAGGIT_SELECTIZE['MINIMUM_QUERY_LENGTH'],
            'recommendation_limit': settings.TAGGIT_SELECTIZE['RECOMMENDATION_LIMIT'],
            'diacritics': "true" if settings.TAGGIT_SELECTIZE['DIACRITICS'] else "false",
            'create': "true" if settings.TAGGIT_SELECTIZE['CREATE'] else "false",
            'persist': "true" if settings.TAGGIT_SELECTIZE['PERSIST'] else "false",
            'open_on_focus': "true" if settings.TAGGIT_SELECTIZE['OPEN_ON_FOCUS'] else "false",
            'hide_selected': "true" if settings.TAGGIT_SELECTIZE['HIDE_SELECTED'] else "false",
            'close_after_select': "true" if settings.TAGGIT_SELECTIZE['CREATE'] else "false",
            'load_throttle': settings.TAGGIT_SELECTIZE['LOAD_THROTTLE'],
            'preload': "true" if settings.TAGGIT_SELECTIZE['PRELOAD'] else "false",
            'add_precedence': "true" if settings.TAGGIT_SELECTIZE['ADD_PRECEDENCE'] else "false",
            'select_on_tab': "true" if settings.TAGGIT_SELECTIZE['SELECT_ON_TAB'] else "false",
            'plugins': ",".join(["\"{}\"".format(plugin) for plugin in js_plugins]),
            'remote_url': reverse('tags_recommendation')
        }
        return mark_safe("\n".join([html, js]))

    class Media:
        css = {
            'all': settings.TAGGIT_SELECTIZE['CSS_FILENAMES']
        }
        js = settings.TAGGIT_SELECTIZE['JS_FILENAMES']
