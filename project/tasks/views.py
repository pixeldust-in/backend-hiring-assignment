from django.shortcuts import render, get_object_or_404
from tasks.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
import datetime

from tasks.models import Project, Task
from .forms import ProjectForm, UpdateProjectForm, CreateTaskForm, UpdateTaskForm


def index(request):
    return render(request,'tasks/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'tasks/registration.html', {'user_form':user_form, 'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect("/tasks/projects/")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'tasks/login.html', {})


def get_projects(request):
    if request.user.is_authenticated:
        project_data = []
        projects = Project.objects.filter(client = request.user, end_date__gte=datetime.datetime.today())
        for project in projects:
            data = {}
            data["id"] = project.id
            data["project_name"] = project.name
            data["description"] = project.description
            data["start_date"] = project.start_date
            data["end_date"] = project.end_date
            project_data.append(data)
            
        context = {"projects": project_data}
        return render(request, "tasks/projects.html", context)
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def create_project(request):
    context = {}
    if request.user.is_authenticated:
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/projects/")

        context.update({"form": form})
        return render(request, "tasks/create_project.html", context)
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def update_project(request, id):
    context = {}
    if request.user.is_authenticated:
        obj = get_object_or_404(Project, id=id)

        form = UpdateProjectForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/tasks/projects/")
        context["form"] = form
    
        return render(request, "tasks/update_project.html", context)
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def delete_project(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Project, id=id)
        obj.delete()
        return redirect("/tasks/projects/")
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def get_tasks(request, project_id):
    if request.user.is_authenticated:
        project = Project.objects.get(id=project_id)
        task_data = []
        tasks = Task.objects.filter(project=project)
        for task in tasks:
            data = {}
            data["id"] = task.id
            data["task_name"] = task.name
            data["description"] = task.description
            data["status"] = task.status
            data["project_name"] = project.name
            task_data.append(data)
        
        context = {"tasks": task_data}
        return render(request, "tasks/tasks.html", context)
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def create_task(request, project_id):
    context = {}
    if request.user.is_authenticated:
        project = Project.objects.get(id=project_id)
        form = CreateTaskForm(request.POST, project)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.project = project
            obj.save()
            return redirect("/tasks/projects/")

        context.update({"form": form})
        return render(request, "tasks/create_tasks.html", context)
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def update_task(request, id):
    context = {}
    if request.user.is_authenticated:
        obj = get_object_or_404(Task, id=id)

        form = UpdateTaskForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/tasks/projects/")
        context["form"] = form
    
        return render(request, "tasks/update_task.html", context)
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)


def delete_task(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Task, id=id)
        obj.delete()
        return redirect("/tasks/projects/")
    else:
        return JsonResponse({"status": False, "message": "Login to continue"}, status=400)
