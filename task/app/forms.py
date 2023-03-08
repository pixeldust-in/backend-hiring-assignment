from django import forms
from .models import Task,Project

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'