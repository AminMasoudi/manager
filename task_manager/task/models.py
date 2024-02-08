from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timesince

import uuid
# Create your models here.

class Task(models.Model):

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
    
    class STATE_CHOICES(models.IntegerChoices):
        TODO = 1
        In_progress = 2
        Blocked = 3
        Done = 4

    class PRIORITY_CHOICES(models.IntegerChoices):
        LOW = 0
        NORMAL = 1
    
    id = models.UUIDField(
        primary_key= True,
        default=uuid.uuid4,
        editable=False
    )
    
    title = models.CharField(_("Title"), max_length=128)

    description = models.TextField(
        _("Description"),
        max_length=2000,
        null=True,
        blank=True
        )

    deadline = models.DateTimeField(
        _("Deadline"),
        null=True,
        blank=True
        )


    state = models.IntegerField(
        _("State"),
        choices=STATE_CHOICES,
        default=STATE_CHOICES.TODO
        )
    
    priority = models.IntegerField(
        _("Priority"),
        choices=PRIORITY_CHOICES,
        default = PRIORITY_CHOICES.LOW
        )
    created_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.title

    @property
    def until(self):
        if self.deadline is None:
            return 
        return timesince.timeuntil(
            self.deadline
        )

    def done(self) -> bool:
        return self.state == self.STATE_CHOICES.Done
    done.boolean = True
    