from django.urls import path, include

from causes.views import objective_update, objective_delete

urlpatterns = [
    path('objectives/', include(([
        path('<int:pk>/', objective_update, name='update'),
        path('<int:pk>/delete/', objective_delete, name='delete'),
    ], 'objectives'))),
]
