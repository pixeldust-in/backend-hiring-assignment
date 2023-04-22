from django.db import models

# Create your models here.

# client Model

class ClientModel(models.Model):
    clientname = models.CharField(max_length=100)

    def __str__(self):
        return self.clientname
    

# Project Model

class ProjectModel(models.Model):
    projectname = models.CharField(max_length=100)
    p_descrption = models.TextField()
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    startdate = models.DateField(auto_now=True)
    enddate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.projectname
    

# Task Model

class TaskModel(models.Model):
    taskname = models.CharField(max_length=100)
    t_description = models.TextField()
    projectname = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


