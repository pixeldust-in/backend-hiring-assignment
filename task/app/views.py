from django.shortcuts import render, redirect
from .forms import TaskForm,ProjectForm
from .models import Task, Project
import datetime



#Views For Tasks

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'app/list.html',{
        'tasks':tasks
    })



def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/app/task_list/')
            except:
                pass
    else:
        form = TaskForm()

    return render(request,'app/add.html',{'form':form})



def edit_task(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                return redirect('/app/task_list/')
            except:
                pass
    else:
        form = TaskForm(instance=task)
    
    return render(request,'app/add.html',{'form':form})



def delete_task(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('/app/task_list/')
                


#Views For Projects

def project_list(request):
    projects = Project.objects.filter(end_date__gt = datetime.date.today())
    return render(request,'app/projects.html',{
        'projects':projects
    })


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/app/projects/')
            except:
                pass
    else:
        form = ProjectForm()

    return render(request,'app/add_project.html',{'form':form})


def delete_project(request,pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return redirect('/app/projects/')


def edit_project(request,pk):
    task = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=task)
        if form.is_valid():
            try:
                form.save()
                return redirect('/app/projects/')
            except:
                pass
    else:
        form = ProjectForm(instance=task)
    
    return render(request,'app/add_project.html',{'form':form})


def project_task(request,pk):
    task = Task.objects.filter(project=pk)

    return render(request,'app/project_task.html',{'tasks':task})



def index(request):
    urls = {
        'To List all Tasks' : '/app/task_list/',
        'To List all Projects ' : '/app/projects/',
        'To Delete Task' : '/app/delete_task/<id>',
        'To Delete Project' : '/app/delete_project/<id>',
        'To Edit Task' : '/app/edit_task/<id>',    
        'To Edit Project' : '/app/edit_project/<id>',
        'To add new Task' : '/app/new_task/',
        'To add new Project' : '/app/add_project/',  
        'To List all Tasks (DRF)' : '/api/task_list/',
        'To List all Projects (DRF)' : '/api/project_list/',
        'TO Perform CRUD operations on Tasks (DRF)' : '/api/task_list/<id>',
        'TO Perform CRUD operations on Projects (DRF)' : '/api/project_list/<id>',
    }
    return render(request,'app/index.html',{'urls':urls})