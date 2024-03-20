from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from task.models import Task


class Command(BaseCommand):
    help = "Initialize the task app"

    def handle(self, *args: Any, **options: Any) -> str | None:
        print("create user_tasks group")
        base_user_group = Group.objects.create(name="task_users")
        base_user_group.permissions.set(self.some_perms())
        base_user_group.save()

    def some_perms(self):
        content_type = ContentType.objects.get_for_model(Task)
        permission = Permission.objects.filter(
            content_type=content_type,
        )
        return permission
