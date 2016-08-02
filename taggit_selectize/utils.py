# Miscellaneous utilities
from django.utils import six
from django.utils.encoding import force_text
from taggit.utils import split_strip


def parse_tags(tagstring):
    """
    Parses tag input, with multiple word input being activated and
    delineated by commas and double quotes. Quotes take precedence, so
    they may contain commas.

    Returns a sorted list of unique tag names.

    Adapted from Taggit, modified to not split strings on spaces.

    Ported from Jonathan Buchanan's `django-tagging
    <http://django-tagging.googlecode.com/>`_
    """
    if not tagstring:
        return []

    tagstring = force_text(tagstring)

    words = []
    buffer = []
    # Defer splitting of non-quoted sections until we know if there are
    # any unquoted commas.
    to_be_split = []
    i = iter(tagstring)
    try:
        while True:
            c = six.next(i)
            if c == '"':
                if buffer:
                    to_be_split.append(''.join(buffer))
                    buffer = []
                c = six.next(i)
                while c != '"':
                    buffer.append(c)
                    c = six.next(i)
                if buffer:
                    word = ''.join(buffer).strip()
                    if word:
                        words.append(word)
                    buffer = []
            else:
                buffer.append(c)
    except StopIteration:
        # If we were parsing an open quote which was never closed treat
        # the buffer as unquoted.
        if buffer:
            to_be_split.append(''.join(buffer))
    if to_be_split:
        for chunk in to_be_split:
            words.extend(split_strip(chunk, ','))
    words = list(set(words))
    words.sort()
    return words


