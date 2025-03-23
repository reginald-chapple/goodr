from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from causes.models import Cause

class Project(BaseModel):
    
    PROJECT_STATUS = (
        ('Draft', 'Draft'),
        ('Proposed', 'Proposed'),
        ('Funding', 'Funding'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(_("title"), max_length=100, null=False, blank=True)
    description = models.TextField(_("description"), default="", null=False, blank=True)
    intended_impact = models.TextField(_("intended impact"), default="", null=False, blank=True)
    beneficaries = models.TextField(_("beneficiaries"), default="", null=False, blank=True)
    target_amount = models.DecimalField(_("target amount"), max_digits=10, decimal_places=2, null=False, blank=True)
    current_amount = models.DecimalField(_("current amount"), max_digits=10, decimal_places=2, default=0, null=False, blank=True)
    status = models.CharField(_("status"), max_length=12, choices=PROJECT_STATUS, default="Draft", null=False, blank=True)
    location = models.CharField(_("location"), max_length=100, null=False, blank=True)
    deadline = models.DateField(_("deadline"), null=False, blank=True)
    completion_date = models.DateField(_("completion date"), null=True, blank=True)
    cause = models.ForeignKey(Cause, verbose_name=_("cause"), on_delete=models.CASCADE, related_name="projects", null=False, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("created by"), on_delete=models.CASCADE, related_name="projects", null=False, blank=True)

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})

class ProjectParticipant(BaseModel):
    PROJECT_ROLE = (
        ('Orgainizer', 'Orgainizer'),
        ('Volunteer', 'Volunteer'),
        ('Follower', 'Follower'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="project_participation", null=False, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="project_participants", null=False, blank=True)
    role = models.CharField(_("role"), max_length=10, choices=PROJECT_ROLE, default="Follower", null=False, blank=True)
    
    

    class Meta:
        verbose_name = _("project participant")
        verbose_name_plural = _("project participants")

    def __str__(self):
        return f"{self.project.title } - {self.user.username} ({self.role})"
        

    def get_absolute_url(self):
        return reverse("projectparticipant_detail", kwargs={"pk": self.pk})

class ProjectUpdate(BaseModel):
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="project_updates", null=False, blank=True)
    content = models.TextField(_("content"), default="", null=False, blank=True)
    

    class Meta:
        verbose_name = _("project update")
        verbose_name_plural = _("project updates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_update_detail", kwargs={"pk": self.pk})
