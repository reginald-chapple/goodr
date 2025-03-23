import decimal
from decimal import Decimal

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from causes.models import Project

class Objective(BaseModel):

    description = models.CharField(
        max_length=255,
        help_text="A clear description of the objective.",
        null=False,
        blank=True
    )
    target_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The specific, measurable target to be achieved."
    )
    unit_of_measurement = models.CharField(
        max_length=50,
        blank=True,
        help_text="The unit in which the target is measured (e.g., 'cans', 'trees', 'students', 'hours')."
    )
    deadline = models.DateField(
        null=True,
        blank=True,
        help_text="The deadline for achieving this objective."
    )
    current_progress = models.IntegerField(
        default=0,
        help_text="The current progress towards the target (numerical value)."
    )
    notes = models.TextField(
        blank=True,
        help_text="Any additional notes or updates on this objective."
    )
    is_completed = models.BooleanField(
        default=False,
        help_text="Indicates if this objective has been completed."
    )
    completion_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The date and time when this objective was completed."
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="objectives",
        help_text="The project associated with this objective.",
        null=False,
        blank=True
    )

    class Meta:
        verbose_name = _("objective")
        verbose_name_plural = _("objectives")

    def __str__(self):
        return f"{self.description} ({self.target_value} {self.unit_of_measurement})"

    def get_absolute_url(self):
        return reverse("objective_detail", kwargs={"pk": self.pk})
    
    @property
    def percentage_complete(self):
        """Calculates the percentage of completion for the objective."""
        try:
            target = self.target_value
            progress = Decimal(self.current_progress)  # Ensure progress is also a Decimal for consistency
            if target > 0:
                return (progress / target) * 100
            elif target == Decimal('0'):
                return 100 if progress >= 0 else 0
            else:
                return 0
        except (TypeError, ValueError, decimal.InvalidOperation):
            return 0
