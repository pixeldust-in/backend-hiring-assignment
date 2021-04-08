from django.db import models
from django.contrib.auth.models import User



STATUS = (('TODO' , 'TODO') , ('WIP' , 'WIP') , ('ONHOLD' , 'ONHOLD') , ('DONE' , 'DONE')) 


class Project(models.Model):
    project_name = models.CharField(max_length=1000)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    client = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=1000)
    task_description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=100 , choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.task_name + ' - ' + self.project.project_name
    