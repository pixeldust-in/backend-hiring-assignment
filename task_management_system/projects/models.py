from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    start_data = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.project_name
    
class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField(max_length=30)
    location = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.client_name
