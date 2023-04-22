from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models import ClientModel, ProjectModel, TaskModel
from .forms import ProjectForm, TaskForm, ClientForm
from django.contrib import messages
from datetime import datetime

# Create your views here.


## View for home page

class home(View):
    def get(self,request):

        to_day = datetime.now().strftime('%m/%d/%Y')
        today = datetime.strptime(to_day,'%m/%d/%Y')

        data = ProjectModel.objects.filter(enddate__range=[today,'2050-12-31'])
        data1 = ProjectModel.objects.filter(enddate=None)

        context = {'data' : data, 'data1':data1}
        return render(request, 'TaskManagementApp/home.html', context)
    
    
## View for delete project

class deleteproject(View):
    def get(self,request,id):
        data = ProjectModel.objects.get(id=id)
        data.delete()
        return redirect('home')
    
    
## View for add project

class addproject(View):
    def get(self,request):
        form1 = ClientForm()
        form = ProjectForm()
        data = ClientModel.objects.all()

        context = {'form1':form1, 'form':form, 'data':data}

        return render(request,'TaskManagementApp/addproject.html', context)
    
    def post(self,request):
        form1 = ClientForm()
        form = ProjectForm()
        data = ClientModel.objects.all()
        context = {'form1':form1, 'form':form, 'data': data}
        

        edate = request.POST['enddate']
        end_date = datetime.strptime(edate,'%m/%d/%Y')

        to_day = datetime.now().strftime('%m/%d/%Y')
        today = datetime.strptime(to_day,'%m/%d/%Y')


        if request.method == 'POST':
            if str(today)>str(end_date):
                messages.warning(request,'End date is smaller than today')
                return render(request,'TaskManagementApp/addproject.html', context)

            elif str(today) == str(end_date):
                messages.warning(request,'End date and today date cannot be same')
                return render(request,'TaskManagementApp/addproject.html', context)

            else:


                form = ProjectForm(request.POST)

                if form.is_valid():
                    form.save()

                    messages.success(request,'Project Added Successfully')
                    return redirect('home')
            
        return render(request,'TaskManagementApp/addproject.html', context)


## View for add client

class addclient(View):
    def post(self,request):
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('addproject')
            
        messages.warning(request, 'Something Went Wrong')
        return redirect('home')
    


## View for add task           

class addtask(View):
    def get(self,request):
        form = TaskForm()
        data = ProjectModel.objects.all()

        context = {'form':form, 'data':data}
        return render(request,'TaskManagementApp/addtask.html', context)
    
    def post(self,request):
        form = TaskForm()
        data = ProjectModel.objects.all()

        if request.method == 'POST':
            form = TaskForm(request.POST)

            if form.is_valid():
                form.save()

                messages.success(request,'Task Added Successfully')
                return redirect('home')
            
        context = {'form':form, 'data':data}
        return render(request,'TaskManagementApp/addtask.html', context)
    


 ## View for View all Task   

class viewtask(View):
    def get(self,request):
        data = TaskModel.objects.all()

        context = {'data':data}
        return render(request,'TaskManagementApp/viewtask.html', context)



## View for Delete task

class deletetask(View):
    def get(self,request,id):
        data = TaskModel.objects.get(id=id)
        data.delete()
        return redirect('home')
    


 ## View for project task   
    
class viewprojecttask(View):
    def get(self,request,id):
        data = TaskModel.objects.filter(projectname=id)
        
        context = {'data':data}
        return render(request,'TaskManagementApp/viewprojecttask.html', context)
    


## View for edit project

class editproject(View):
    def get(self,request,id):
        data = ProjectModel.objects.get(id=id)
        form = ProjectForm()

        context = {'data':data,'form':form}
        return render(request,'TaskManagementApp/editproject.html', context)
    
    def post(self,request,id):

        data = ProjectModel.objects.get(id=id)
        form = ProjectForm()

        context = {'data':data, 'form':form}

    
        if request.method == 'POST':

            edate = request.POST['enddate']
            end_date = datetime.strptime(edate,'%m/%d/%Y')

            to_day = datetime.now().strftime('%m/%d/%Y')
            today = datetime.strptime(to_day,'%m/%d/%Y')


            if request.method == 'POST':

                if str(today)>str(end_date):
                    messages.warning(request,'End date is smaller than today')
                    return render(request,'TaskManagementApp/editproject.html', context)

                elif str(today) == str(end_date):
                    messages.warning(request,'End date and today date cannot be same')
                    return render(request,'TaskManagementApp/editproject.html', context)
                
                else:
                    updated_date = ProjectModel.objects.get(id=id)
                    updated_date.enddate = end_date
                    updated_date.save()
                    return redirect('home')
            
        return render(request,'TaskManagementApp/editproject.html', context)
        



## View for edit task

class edittask(View):
    def get(self,request,id):
        data = TaskModel.objects.get(id=id)
        form = TaskForm()

        context = {'data':data, 'form':form}
        return render(request,'TaskManagementApp/edittask.html', context)

    def post(self,request,id):

        data = TaskModel.objects.get(id=id)
        form = TaskForm()


        if request.method == 'POST':

            updated_status = TaskModel.objects.get(id=id)
            updated_status.status = request.POST['status']
            updated_status.save()
            return redirect('home')
            
        context = {'data':data, 'form':form}
        return render(request,'TaskManagementApp/edittask.html', context)



 ## View for All projects   

class allproject(View):
    def get(self,request):
        data = ProjectModel.objects.all()

        context = {'data':data}

        return render(request,'TaskManagementApp/allproject.html', context)




       

