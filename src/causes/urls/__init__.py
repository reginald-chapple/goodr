from django.urls import path, include

urlpatterns = [
    path('', include('causes.urls.projects')),
    path('', include('causes.urls.project_management')),
    path('', include('causes.urls.objectives')),
    path('', include('causes.urls.assignments')),
]
