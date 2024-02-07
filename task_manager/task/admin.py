from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "state",
        "priority",
        "done",
        "until",
        "deadline",
        )
    list_display_links = "title", 
    actions = (
        "state_to_todo",
        "state_to_in_progress",
        "state_to_blocked",
        "state_to_done",
    )
    actions_on_bottom = True

    list_editable = "priority", "state"

    list_filter = "state", "priority"

    @admin.action(description="Done")
    def state_to_done(self, request, queryset):
        queryset.update(
            state=Task.STATE_CHOICES.Done
        )

    @admin.action(description="TODO")
    def state_to_todo(self, request, queryset):
        queryset.update(
            state=Task.STATE_CHOICES.TODO
        )

    @admin.action(description="Blocked")
    def state_to_blocked(self, request, queryset):
        queryset.update(
            state=Task.STATE_CHOICES.Blocked
        )
    @admin.action(description="In_progress")
    def state_to_in_progress(self, request, queryset):
        queryset.update(
            state=Task.STATE_CHOICES.In_progress
        )    

    # TODO : add filters 
    # TODO : add search fields
    # TODO : add ordering
    # TODO : add fieldsets
    # TODO : add inlines

        