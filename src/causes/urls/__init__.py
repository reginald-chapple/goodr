from django.urls import path, include

urlpatterns = [
    path('', include('causes.urls.projects')),
    path('', include('causes.urls.project_management')),
]