from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "state",
        "priority",
        "until",
        "deadline",
        )
    list_display_links = "title", 
    # TODO : add action
    # TODO : add filters
     