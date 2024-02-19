from typing import Iterable
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from task.models import Task
# Create your models here.


class User(AbstractUser):
    def save(self, *args, **kwargs) -> None:
        base_user_group = Group.objects.filter(name="Base_Users").all()
        print(base_user_group)
        if  len(base_user_group)==0:
            base_user_group = Group.objects.create(name="Base_Users")
            base_user_group.permissions.set(self.perm())
        self.is_staff = True
        return super().save(*args, **kwargs)

    def perm(self):
        content_type = ContentType.objects.get_for_model(Task)
        permission = Permission.objects.filter(
            content_type=content_type,
        )
        return permission
