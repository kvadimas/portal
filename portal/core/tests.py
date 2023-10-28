from http import HTTPStatus

from django.test import Client, TestCase


class CoreTestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_not_found(self):
        """Проверка страницы 404"""
        response = self.guest_client.get("/very-very-very-very-very-very-bad-url/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
