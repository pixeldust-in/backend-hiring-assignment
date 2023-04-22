from django.contrib import admin
from .models import ClientModel, ProjectModel, TaskModel

# Register your models here.

# Register client model

@admin.register(ClientModel)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','clientname']


# Register project model

@admin.register(ProjectModel)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','projectname','p_descrption','client','startdate','enddate']


# Register task model

@admin.register(TaskModel)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','taskname','t_description','projectname','status']