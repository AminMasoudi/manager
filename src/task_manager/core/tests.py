from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group


class TestUser(TestCase):
    def setUp(self) -> None:
        Group.objects.create(name="task_users")

        return super().setUp()

    def test_create(self):
        test_model = User.objects.create_user(
            username="pass", email="pass@pass.com", password="pass"
        )
        self.assertEqual(test_model.username, "pass")
        self.assertEqual(test_model.email, "pass@pass.com")
        assert test_model.groups.filter(name="task_users").exists()
        try:
            User.objects.create_user()
            assert False, "must raise ValidationError with saving User with no username"

        except TypeError as e:
            pass
