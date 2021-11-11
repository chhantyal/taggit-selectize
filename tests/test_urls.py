from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    def test_urls(self):
        response = self.client.get(reverse('tags_recommendation'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request['PATH_INFO'], '/')
