from django.contrib import admin

from causes.models import (
    Cause,
    Project,
    ProjectParticipant,
    ProjectUpdate,
    Objective,
    UserCause,
    Donation
)

admin.site.register(Cause)
admin.site.register(Project)
admin.site.register(ProjectParticipant)
admin.site.register(ProjectUpdate)
admin.site.register(Objective)
admin.site.register(UserCause)
admin.site.register(Donation)

