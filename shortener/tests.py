from django.test import TestCase
from .models import Links

class URLModelTest(TestCase):

    def test_generate_short_url(self):
        url = Links()
        short_url = url.generate_short_url()
        self.assertEqual(len(short_url), 7)
        self.assertTrue(short_url.isalnum())

    def test_save_method_generates_short_url(self):
        original_url = "https://example.com"
        url = Links(original_url=original_url)
        url.save()
        self.assertIsNotNone(url.short_url)
        self.assertEqual(len(url.short_url), 7)
        self.assertTrue(url.short_url.isalnum())

    def test_unique_short_url(self):
        original_url1 = "https://example1.com"
        original_url2 = "https://example2.com"
        url1 = Links(original_url=original_url1)
        url2 = Links(original_url=original_url2)
        url1.save()
        url2.save()
        self.assertNotEqual(url1.short_url, url2.short_url)
