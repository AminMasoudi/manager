from typing import Iterable
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import UserManager

# Create your models here.


class User(AbstractUser):

    def save(self, *args, **kwargs) -> None:
        task_user_group = Group.objects.filter(name="task_users").first()
        # assign task_user group to user
        if task_user_group is None:
            raise ValueError("task_users group is not found. run init_task_app command")
        r = super().save(*args, **kwargs)
        self.groups.add(task_user_group)
        self.is_staff = True
        return r

    objects = UserManager()
