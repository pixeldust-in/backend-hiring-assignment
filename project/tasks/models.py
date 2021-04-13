from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    client = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS = (
        ('TODO', 'TODO'),
        ('WIP', 'WIP'),
        ('ONHOLD', 'ONHOLD'),
        ('DONE' , 'DONE')
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=50 , choices=STATUS)

    def __str__(self):
        return f"{self.project.name} - {self.name}"