from django.test import TestCase, RequestFactory

from categories.views import create

__all__ = ['ViewTestCase']


class ViewTestCase(TestCase):
    def setUp(self):
        super(TestCase, self).setUp()

        self.request_factory = self.factory = RequestFactory()

    def test_bad_request(self):
        request = self.request_factory.get('')
        response = create(request)

        self.assertEqual(200, response.status_code)
