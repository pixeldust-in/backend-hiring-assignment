from django.db import models

# Create your models here.
from projects.models import Project

class Task(models.Model):
    STATUS_CHOICES = (
        ('TODO', 'To Do'),
        ('WIP', 'Work in Progress'),
        ('ONHOLD', 'On Hold'),
        ('DONE', 'Done'),
    )

    task_name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return self.task_name
