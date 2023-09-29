from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'all_tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['task_name', 'description', 'project', 'status']
    success_url = '/tasks/'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['task_name', 'description', 'project', 'status']
    success_url = '/tasks/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = '/tasks/'
