from django.urls import path
from. import views

urlpatterns = [
    # Url for Landing Screen for the Task Manager Website
    path('',views.home.as_view(),name='home'),
    
    path('deleteproject/<int:id>',views.deleteproject.as_view(),name='deleteproject'), # to delete project

    path('addproject',views.addproject.as_view(),name='addproject'), # to add project
    
    path('viewtask/<int:id>',views.viewtask.as_view(),name='viewtask'), # to View project
    
    path('addtask',views.addtask.as_view(),name='addtask'), # to add task in project
    
    path('deletetask/<int:id>',views.deletetask.as_view(),name='deletetask'), # to delete task in project
    
    path('edittask/<int:id>',views.edittask.as_view(),name='edittask'), # to edit task in project
    
    path('addclient',views.addclient.as_view(),name='addclient'), # to add client
    
    path('viewalltask',views.viewalltask.as_view(),name='viewalltask'), # to view all task in all project
    
    path('editproject/<int:id>',views.editproject.as_view(),name='editproject'), # to edit project enddate
    
    path('viewallproject',views.viewallproject.as_view(),name='viewallproject'),  # to all project

]
