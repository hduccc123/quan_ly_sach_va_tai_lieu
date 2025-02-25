from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    