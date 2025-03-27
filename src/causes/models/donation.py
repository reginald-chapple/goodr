from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from causes.models import Project

class Donation(BaseModel):

    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2, null=False, blank=True)
    message = models.TextField(_("message"), default="", null=False, blank=True)
    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name="donations", null=False, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, related_name="donations", null=False, blank=True)

    class Meta:
        verbose_name = _("donation")
        verbose_name_plural = _("donations")

    def __str__(self):
        return f"{self.user.username} donated {self.amount} to {self.project.title}"

    def get_absolute_url(self):
        return reverse("donation_detail", kwargs={"pk": self.pk})
