from django.urls import path
from . import views
urlpatterns = [

    #Urls for tasks
    path('task_list/',views.TaskListView.as_view(),name='task_list'),
    path('task_list/<str:pk>/',views.TaskDetailView.as_view(),name='task_list'),


    #Urls for projects
    path('project_list/',views.ProjectListView.as_view(),name='project_list'),
    path('project_list/<str:pk>/',views.ProjectDetailView.as_view(),name='all')

]
    