from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Task(models.Model):

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
    
    class STATE_CHOICES(models.IntegerChoices):
        TODO = 0

    class PRIORITY_CHOICES(models.IntegerChoices):
        LOW = 0
        NORMAL = 1

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
        return 2    #TODO: calculate the remaining days
    