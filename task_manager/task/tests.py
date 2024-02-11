from django.test import TestCase
from .models import Task
from django.core.exceptions import ValidationError
# TODO: Test for create save and update methods
# Create your tests here.

class TestTask(TestCase):
    def test_create(self):
        test_model = Task.objects.create(
            title="pass"
        )

        self.assertEqual(
            test_model.priority,
            Task.PRIORITY_CHOICES.LOW
        )
        self.assertEqual(
            test_model.state,
            Task.STATE_CHOICES.TODO
        )
        try:
            Task.objects.create()
            assert False, \
                "must raise ValidationError with saving Task with no title"
            
        except ValidationError as e:
            pass
        
            
