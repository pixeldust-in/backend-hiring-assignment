from django.shortcuts import render
from .models import Project, Client
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ClientForm


def homepage(request):
    return render(request, 'projects/home.html')

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'all_project' # name of object of all the projects
    
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['project_name', 'description', 'client', 'end_date']
    success_url = '/projects/' # redirect url
    
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['project_name', 'description', 'client', 'end_date']
    success_url = '/projects/'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_deleted.html'
    success_url = '/projects/' 
    
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'projects/client_form.html'
    success_url = '/projects/'
    