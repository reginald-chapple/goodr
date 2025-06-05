from django.urls import path, include

from causes.views import assignment_update, assignment_delete

urlpatterns = [
    path('assignments/', include(([
        path('<int:pk>/', assignment_update, name='update'),
        path('<int:pk>/delete/', assignment_delete, name='delete'),
    ], 'assignments'))),
]
