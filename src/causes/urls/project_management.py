from django.urls import path, include

from causes.views import (
    project_create, 
    project_detail, 
    project_update, 
    project_delete, 
    my_projects,
    project_objectives,
    objective_create,
    project_assignments,
    assignment_create
)

urlpatterns = [
    path('manage-projects/', include(([
        path('', my_projects, name='my_projects'),
        path('create/', project_create, name='create'),
        path('<int:pk>/', project_detail, name='detail'),
        path('<int:pk>/update/', project_update, name='update'),
        path('<int:pk>/delete/', project_delete, name='delete'),
        path('<int:pk>/objectives/', project_objectives, name='objectives'),
        path('<int:pk>/objectives/create/', objective_create, name='objective_create'),
        path('<int:pk>/assignments/', project_assignments, name='assignments'),
        path('<int:pk>/assignments/create/', assignment_create, name='assignment_create'),
    ], 'project-management'))),
]