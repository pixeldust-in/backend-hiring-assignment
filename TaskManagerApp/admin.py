from django.contrib import admin
from.models import ClientModel, ProjectModel, TaskModel

# Register your models here.

# Registering Admin for Client Model
@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display=['id','ClientName']



# Registering Admin for Project Model
@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','ProjectName','PDescription','Client','StartDate','EndDate']



# Registering Admin for Task Model
@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','TaskName','TDescription','Project','Status']