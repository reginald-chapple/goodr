from django.urls import path, include

from causes.views import project_create, project_detail, project_list, project_update, project_delete, my_projects

urlpatterns = [
    path('projects/', include(([
        path('', project_list, name='project_list'),
        path('my-projects/', my_projects, name='my_projects'),
        path('create/', project_create, name='project_create'),
        path('<int:pk>/', project_detail, name='project_detail'),
        path('<int:pk>/update/', project_update, name='project_update'),
        path('<int:pk>/delete/', project_delete, name='project_delete'),
    ], 'projects'))),
]