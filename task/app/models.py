from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name
    


class Project(models.Model):
    name = models.CharField(max_length=120)
    client = models.CharField(max_length=120)
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.name



STATUS_CHOICES = (
    ("TODO", "TODO"),
    ("WIP", "WIP"),
    ("ONHOLD", "ONHOLD"),
    ("DONE", "DONE"),

)

class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=250)
    status = models.CharField(choices=STATUS_CHOICES,default='TODO',max_length=20)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')

    def __str__(self) -> str:
        return self.name

