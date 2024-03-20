from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

class TestUser(TestCase):
    def test_create(self):
        test_model = User.objects.create(
            username="pass",
            email="pass@pass.com",
            password="pass"
        )
        self.assertEqual(
                test_model.username,
                "pass"
            )
        self.assertEqual(
                test_model.email,
                "pass@pass.com"
            )
        try:
            User.objects.create()
            assert False, \
                "must raise ValidationError with saving User with no username"

        except ValidationError as e:
            pass
        