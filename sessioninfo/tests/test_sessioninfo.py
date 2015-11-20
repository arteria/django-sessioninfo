"""Tests for the models of the sessioninfo app."""
from django.contrib.auth.models import User
from django.test import TestCase, Client

class SessionInfoTests(TestCase):

    def setUp(self):
        self.user_username = 'user'
        self.user_email = 'user@example.com'
        self.user_password = 'user_pw'
        self.user = User.objects.create_user(self.user_username, self.user_email, self.user_password)

        self.client = Client()
        self.client.login(username=self.user_username, password=self.user_password)

    def test_get_session_user(self):
        s = self.client.session
        s.save()
        session_key = s.session_key
        response = self.client.post('/get-session-user/', {'session_key': session_key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.content), self.user.id)