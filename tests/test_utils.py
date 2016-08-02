from django.test import TestCase
from taggit.models import Tag

from taggit_selectize.utils import parse_tags, join_tags


class TestUtils(TestCase):
    def test_tag_parser(self):
        self.assertListEqual(parse_tags('foo, bar, baz'), ['bar', 'baz', 'foo'])

    def test_tag_parser_not_space_delimited(self):
        self.assertListEqual(parse_tags('foo bar'), ['foo bar'])

    def test_tag_parser_quoted(self):
        self.assertListEqual(parse_tags('"foo bar"'), ['foo bar'])

    def test_tag_parser_multiple_quoted(self):
        self.assertListEqual(parse_tags('"foo bar", "baz bongo"'), ['baz bongo', 'foo bar'])

    def test_tag_parser_dangling_quote(self):
        self.assertListEqual(parse_tags('"foo bar'), ['foo bar'])

    def test_tag_parser_quotes_take_precedence_over_commas(self):
        self.assertListEqual(parse_tags('"foo, bar"'), ['foo, bar'])

    def test_tag_parser_dangling_quote_with_comma(self):
        self.assertListEqual(parse_tags('"foo, bar'), ['bar', 'foo'])

    def test_tag_parser_dangling_quote_at_end(self):
        self.assertListEqual(parse_tags('foo bar"'), ['foo bar'])

    def test_tag_parser_empty_string(self):
        self.assertListEqual(parse_tags(''), [])

    def test_tag_parser_single_comma(self):
        self.assertListEqual(parse_tags(','), [])

    def test_tag_parser_multiple_commas(self):
        self.assertListEqual(parse_tags(',,,,'), [])

    def test_tag_parser_extra_comma(self):
        self.assertListEqual(parse_tags('foo,,bar'), ['bar', 'foo'])

    def test_tag_parser_extra_opening_quote(self):
        self.assertListEqual(parse_tags('""foo bar"'), ['foo bar'])

    def test_tag_parser_extra_closing_quote(self):
        self.assertListEqual(parse_tags('"foo bar""'), ['foo bar'])

    def test_tag_parser_extra_quotes_and_commas(self):
        self.assertListEqual(parse_tags('""foo,",bar",,baz"""'), [',bar', 'baz', 'foo'])

    def test_tag_joiner(self):
        foo = Tag(name="foo", slug="foo")
        bar = Tag(name="bar", slug="bar")
        self.assertEqual(join_tags([foo, bar]), "bar,foo")

        with self.settings(TAGGIT_SELECTIZE={'DELIMITER': ';'}):
            self.assertEqual(join_tags([foo, bar]), "bar;foo")





