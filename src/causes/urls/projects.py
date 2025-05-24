from django.urls import path, include

from causes.views import project_list, project_view

urlpatterns = [
    path('projects/', include(([
        path('', project_list, name='project_list'),
        path('<int:pk>/', project_view, name='view'),
    ], 'projects'))),
]