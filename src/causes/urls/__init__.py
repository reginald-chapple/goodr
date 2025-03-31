from django.urls import path, include

urlpatterns = [
    path('', include('causes.urls.projects')),
]