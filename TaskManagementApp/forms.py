from django import forms
from .models import ClientModel, ProjectModel, TaskModel

## form for project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        
        fields = ['projectname','p_descrption','client','enddate']

        labels = {
            'projectname' : 'Project Name',
            'p_descrption' : 'Project Description',
            'client' : 'Client Name',
            'enddate' : 'End Date'

        }

Status_Choices = [('TODO','TODO'),('WIP','WIP'),('ONHOLD','ONHOLD'),('DONE','DONE')]
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel

        fields = ['taskname','t_description','projectname','status']

        labels = {
            'taskname' : 'Task Name',
            't_description' : 'Description',
            'projectname' : 'Project Name',
            'status' : 'Status'
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel

        fields = ['clientname',]

        labels = {
            'clientname' : 'Client Name'
        }

        widgets = {
            
            'clientname' : forms.TextInput(attrs={'class':'form-control'})
        }