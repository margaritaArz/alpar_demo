from django.test import SimpleTestCase
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ali_parse_helper.ali_parse_helper.settings")


class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
