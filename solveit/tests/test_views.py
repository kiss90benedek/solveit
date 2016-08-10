from django.test import TestCase
from mock import Mock, patch

from solveit.views import home

__all__ = ['ViewTestCase']


class ViewTestCase(TestCase):
    def setUp(self):
        super(TestCase, self).setUp()

        self.request = Mock()

        today_patcher = patch('solveit.views.helpers.today')
        self.mock_today = today_patcher.start()

    def tearDown(self):
        self.mock_today.stop()

    def test_response_200(self):
        response = home(self.request)

        self.assertEqual(200, response.status_code)

    def test_date(self):
        mock_date_in_bytes = b'mock_date'
        self.mock_today.return_value = mock_date_in_bytes

        response = home(self.request)

        self.assertIn(mock_date_in_bytes, response.content)
