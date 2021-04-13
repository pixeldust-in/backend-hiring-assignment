from django import forms
from django.contrib.auth.models import User
from tasks.models import Project, Task



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = "__all__"


class UpdateProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = "__all__"


class CreateTaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = ["name", "description", "status"]  


class UpdateTaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = "__all__"