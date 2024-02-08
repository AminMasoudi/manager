from django.contrib import admin
from .models import Task
from django.utils.translation import gettext as _
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
    actions = (
        "state_to_todo",
        "state_to_in_progress",
        "state_to_blocked",
        "state_to_done",
    )
    
    readonly_fields = "updated_date", "created_date"
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "title",
                    "description",
                    (
                        "state",
                        "priority"
                    ),
                    "deadline"
                ]
            }
        ),
        
        (
            _("More..."),
            {
                "fields": (
                    "created_date", "updated_date"
                ),
                
                'classes': ('collapse',)
            }
        )
    )

    actions_on_bottom = True

    list_editable = "priority", "state"

    list_filter = (
        "state",
        "priority",
    )

    radio_fields = {"priority": admin.VERTICAL, "state": admin.VERTICAL}

    date_hierarchy = "deadline"
    empty_value_display = '<dev style="color:#70bf2b;">-empty-</dev>' #DONT ASK :)) #BUG css in backend??

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
    
    def get_fieldsets(self, request, obj=None):     #Separate add and change fields
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (
                (
                    None,
                    {
                        "fields":(
                            "title",
                            "description",
                            (
                                "state",
                                "priority"
                            ),
                            "deadline"
                        )
                    }
                ),
            )
        return fieldsets

    # TODO : add search fields
    # TODO : add ordering
    # TODO : add inlines

        