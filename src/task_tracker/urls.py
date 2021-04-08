from django.urls import path
from .views import *

urlpatterns = [
    path('login' , login_attempt , name="login"),
    
    path('home' , home),
    path('project/', ProjectView),
    path('task/' , TaskView)
]
