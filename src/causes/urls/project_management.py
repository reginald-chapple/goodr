from django.urls import path, include

from causes.views import (
    project_create, 
    project_detail, 
    project_update, 
    project_delete, 
    my_projects,
    project_objectives
)

urlpatterns = [
    path('manage-projects/', include(([
        path('', my_projects, name='my_projects'),
        path('create/', project_create, name='create'),
        path('<int:pk>/', project_detail, name='detail'),
        path('<int:pk>/update/', project_update, name='update'),
        path('<int:pk>/delete/', project_delete, name='delete'),
        path('<int:pk>/objectives/', project_objectives, name='objectives'),
    ], 'project-management'))),
]