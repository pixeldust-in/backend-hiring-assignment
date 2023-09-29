from django.db import models

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('TODO', 'TODO'), ('WIP', 'WIP'), ('ONHOLD', 'ONHOLD'), ('DONE', 'DONE')])
