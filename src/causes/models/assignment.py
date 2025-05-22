from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from causes.models import Project

class Assignment(BaseModel):
    ASSIGNMENT_STATUS = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Overdue', 'Overdue'),
    )

    task = models.CharField(_("task"), max_length=50, null=False, blank=True)
    started_at = models.DateTimeField(_("started at"), null=True, blank=True)
    finished_at = models.DateTimeField(_("finished at"), null=True, blank=True)
    due_at = models.DateTimeField(_("due at"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=100, null=False, blank=True)
    notes = models.TextField(_("notes"), default="", null=False, blank=True)
    status = models.CharField(_("status"), max_length=15, choices=ASSIGNMENT_STATUS, default="Pending", null=False, blank=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("assigned to"),
        related_name="assignments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="assignments", null=False, blank=True)

    class Meta:
        verbose_name = _("assignment")
        verbose_name_plural = _("assignments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("assignment_detail", kwargs={"pk": self.pk})
