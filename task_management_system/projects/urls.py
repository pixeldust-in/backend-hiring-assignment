from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ClientCreateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create')    
]
