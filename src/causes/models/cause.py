from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

class Cause(BaseModel):

    name = models.CharField(_("name"), max_length=50, unique=True, null=False, blank=True)
    description = models.TextField(_("description"), default="", null=False, blank=True)

    class Meta:
        verbose_name = _("cause")
        verbose_name_plural = _("causes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cause_detail", kwargs={"pk": self.pk})
