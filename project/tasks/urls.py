from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('projects/', views.get_projects, name='get_projects'),
    path('create-project/', views.create_project, name='create_project'),
    path('update-project/<int:id>', views.update_project, name='update_project'),
    path('delete-project/<int:id>', views.delete_project, name='delete_project'),

    path('get-tasks/<int:project_id>', views.get_tasks, name="get_tasks"),
    path('create-task/<int:project_id>', views.create_task, name="create_task"),
    path('update-task/<int:id>', views.update_task, name="update_task"),
    path("delete-task/", views.delete_task, name="delete_task"),
]