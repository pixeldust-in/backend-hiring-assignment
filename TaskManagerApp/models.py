from django.db import models

# Create your models here.

# Defining Client Model
class ClientModel(models.Model):
    ClientName=models.CharField(max_length=100)

    # return ClientName instead of entire model data.
    def __str__(self):
        return self.ClientName
    


# Defining Project Model
class ProjectModel(models.Model):
    ProjectName=models.CharField(max_length=100)
    PDescription=models.TextField()
    Client=models.ForeignKey(ClientModel,on_delete=models.CASCADE)
    StartDate=models.DateField(auto_now=True)
    EndDate=models.DateField(null=True,blank=True)

    
    # return ClientName instead of entire model data.
    def __str__(self):
        return self.ProjectName


# Defining Task Model
class TaskModel(models.Model):
    TaskName=models.CharField(max_length=100)
    TDescription=models.TextField()
    Project=models.ForeignKey(ProjectModel,on_delete=models.CASCADE)
    Status=models.CharField(max_length=100)