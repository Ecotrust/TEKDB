from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import MagicMock, patch
import json
from login.views import (
    PasswordChangeView as CustomPasswordChangeView,
    index,
    login_logic,
)

User = get_user_model()


class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_index_view(self):
        request = self.factory.get("/")
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Login", response.content.decode("utf-8"))

    def test_login_success(self):
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "testpass123"}
        )
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertIn("explore", response.content.decode("utf-8").lower())
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_credentials(self):
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "wrongpassword"}
        )
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.context["errorcode"], 403)
        self.assertIn("incorrect", response.context["error"].lower())

    def test_login_logic_success(self):
        request = MagicMock()
        request.POST = {"username": "testuser", "password": "testpass123"}
        result = login_logic(request)
        self.assertTrue(result["success"])
        self.assertEqual(result["username"], "testuser")

    def test_login_logic_failure(self):
        request = MagicMock()
        request.POST = {"username": "testuser", "password": "wrongpass"}
        result = login_logic(request)
        self.assertFalse(result["success"])

    def test_login_async(self):
        response = self.client.post(
            reverse("login_async"), {"username": "testuser", "password": "testpass123"}
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data["success"])

    def test_login_async_failure(self):
        response = self.client.post(
            reverse("login_async"), {"username": "testuser", "password": "wrongpass"}
        )
        data = json.loads(response.content)
        self.assertFalse(data["success"])

    def test_password_change_form_invalid_returns_json_errors(self):
        view = CustomPasswordChangeView()
        form = MagicMock()
        form.errors = {"old_password": ["This field is required."]}

        response = view.form_invalid(form)

        self.assertEqual(response.status_code, 400)
        payload = json.loads(response.content)
        self.assertEqual(payload["data"], form.errors)

    @patch("login.views.update_session_auth_hash")
    def test_password_change_form_valid_updates_session_and_returns_success(
        self, mock_update_session_auth_hash
    ):
        view = CustomPasswordChangeView()
        view.request = self.factory.post("/change_password/")
        form = MagicMock()
        form.save.return_value = self.user
        form.is_valid.return_value = True

        response = view.form_valid(form)

        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.content)
        self.assertTrue(payload["data"])
        self.assertEqual(view.object, self.user)
        form.save.assert_called_once_with()
        mock_update_session_auth_hash.assert_called_once_with(view.request, self.user)
