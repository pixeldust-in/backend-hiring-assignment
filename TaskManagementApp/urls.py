from django.urls import path
from .import views

urlpatterns = [

    path('',views.home.as_view(),name='home'),
    path('deleteproject/<int:id>',views.deleteproject.as_view(),name='deleteproject'),
    path('addproject',views.addproject.as_view(),name='addproject'),
    path('addclient',views.addclient.as_view(),name='addclient'),
    path('addtask',views.addtask.as_view(),name='addtask'),
    path('viewtask',views.viewtask.as_view(),name='viewtask'),
    path('deletetask/<int:id>',views.deletetask.as_view(),name='deletetask'),
    path('viewprojecttask/<int:id>',views.viewprojecttask.as_view(),name='viewprojecttask'),
    path('editproject/<int:id>',views.editproject.as_view(),name='editproject'),
    path('edittask/<int:id>',views.edittask.as_view(),name="edittask"),
    path('allproject',views.allproject.as_view(),name='allproject')

]