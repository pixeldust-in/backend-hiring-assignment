from django.urls import path
from . import views

urlpatterns = [

    #Url for Tasks.
    path('task_list/',views.task_list, name='task_list'),
    path('delete_task/<str:pk>/',views.delete_task,name='delete_task'),
    path('edit_task/<str:pk>/',views.edit_task,name='edit_task'),
    path('new_task/',views.new_task,name='new_task'),

    #Urls for project.
    path('projects/',views.project_list,name='project_list'),
    path('delete_project/<str:pk>/',views.delete_project,name='delete_project'),
    path('edit_project/<str:pk>/',views.edit_project,name='edit_project'),
    path('add_project/',views.add_project,name='add_project'),
    path('project_task/<str:pk>/',views.project_task,name='project_task'),


]