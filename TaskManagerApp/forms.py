from django import forms
from.models import ClientModel,ProjectModel,TaskModel


# Defining Project Model Form
class ProjectForm(forms.ModelForm):

    class Meta:
        model=ProjectModel
        fields=['ProjectName','PDescription','Client','EndDate']

        labels={
            'ProjectName':'Project Name',
            'PDescription':'Description',
            'Client':'Client Name',
            'EndDate':'End Date'
        }

        
        widgets={
            'ProjectName':forms.TextInput(attrs={'class':'form-control'}),
            'PDescription':forms.Textarea(attrs={'class':'form-control'}),
            'Client':forms.TextInput(attrs={'class':'form-control'}),
            'EndDate':forms.TextInput(attrs={'class':'form-control'}),
        }

        


# Defining Task Model Form
Status_Choices=[('TODO','TODO'),('WIP','WIP'),('ONHOLD','ONHOLD'),('DONE','DONE')]
class TaskForm(forms.ModelForm):

    Status=forms.ChoiceField(choices=Status_Choices,label='Status',widget=forms.RadioSelect)

    class Meta:
        model=TaskModel
        fields=['TaskName','TDescription','Project','Status']

        labels={
            'TaskName':'Task Name',
            'TDescription':'Task Description',
            'Project':'Project',
            'Status':'Status'
        }

        widgets={
            'TaskName':forms.TextInput(attrs={'class':'form-control'}),
            'TDescription':forms.Textarea(attrs={'class':'form-control'}),
            'Project':forms.TextInput(attrs={'class':'form-control'}),
            'Status':forms.TextInput(attrs={'class':'form-control'}),
        }

# Defining Client Model Form
class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields=['ClientName',]

        labels={
            'ClientName':'Client Name'
        }

        widgets={
            'ClientName':forms.TextInput(attrs={'class':'form-control'})
        }