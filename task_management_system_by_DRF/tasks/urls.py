from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', views.ClientDetail.as_view(), name='client-detail'),
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]
