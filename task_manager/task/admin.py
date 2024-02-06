from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "state",
        "priority",
        "until",
        "deadline",
        )
    list_display_links = "pk", "title"
    # TODO : add action
    # TODO : add filters
     