from django.shortcuts import render ,HttpResponse ,redirect
from django.views import View
from.models import ProjectModel,TaskModel,ClientModel
from.forms import ProjectForm, TaskForm , ClientForm
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

# View for Landing Screen of Task Manager App
class home(View):
    def get(self,request):

        to_day=datetime.now().strftime('%m/%d/%Y')  #to fetch current date datetime module is used
        today=datetime.strptime(to_day,'%m/%d/%Y')  

        data1 = ProjectModel.objects.filter(EndDate__range=[today,'2050-12-31'])  # to show projects whose EndDate is more than Today
        data=ProjectModel.objects.filter(EndDate=None) # to show projects whose EndDate field is None
        context={'data':data,'data1':data1}

        return render(request,'TaskManagerApp/home.html',context)
        

# Delete class to delete Project
class deleteproject(View):
    def get(self,request,id):
        data=ProjectModel.objects.get(id=id)
        data.delete()
        return redirect('home')
    

# Create Project Class
class addproject(View):
    def get(self,request):
        form=ProjectForm()
        form1=ClientForm()
        data=ClientModel.objects.all()
        context={'form':form,'data':data,'form1':form1}
        return render(request,'TaskManagerApp/addproject.html',context)
    
    def post(self,request):
        form=ProjectForm()
        form1=ClientForm()
        data=ClientModel.objects.all()
        context={'form':form,'data':data,'form1':form1}


        if request.method == 'POST':

# try and else block so that if user doesn't select any date website doesn't crash
            try:
                Edate=request.POST['EndDate']
                end_date=datetime.strptime(Edate,'%m/%d/%Y')

                to_day=datetime.now().strftime('%m/%d/%Y')
                today=datetime.strptime(to_day,'%m/%d/%Y')

                # Calculated today and end date so that end should not be smaller or equal to today for a particular project
                if str(today)>str(end_date):
                    messages.warning(request,'End Date smaller than Today')
                    return render(request,'TaskManagerApp/addproject.html',context)
                
                elif str(today)==str(end_date):
                    messages.warning(request,'End Date and Today cannot be same ')
                    return render(request,'TaskManagerApp/addproject.html',context)
                
                else:
                    form=ProjectForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('home')
                    
            except:
                form=ProjectForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home')
                    

        return render(request,'TaskManagerApp/addproject.html',context) 
        

# View Task in Project
class viewtask(View):
    def get(self,request,id):
        data = TaskModel.objects.filter(Project=id)
        return render(request,'TaskManagerApp/viewtask.html',{'data':data})


# Create Task Class
class addtask(View):
    def get(self,request):
        form=TaskForm()
        data=ProjectModel.objects.all()
        context={'form':form,'data':data}
        return render(request,'TaskManagerApp/addtask.html',context)
    

    def post(self,request):
        form=TaskForm()
        data=ProjectModel.objects.all()
        if request.method == 'POST':
            form=TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context={'form':form,'data':data}
        return render(request,'TaskManagerApp/addtask.html',context) 
    


# Delete class to delete task
class deletetask(View):
    def get(self,request,id):
        data=TaskModel.objects.get(id=id)
        data.delete()
        return redirect('home')
    

# Edit Class to Edit a Task
class edittask(View):
    def get(sefl,request,id):
        data=TaskModel.objects.get(id=id)
        form=TaskForm()
        context={'form':form,'data':data}
        return render(request,'TaskManagerApp/edittask.html',context) 


    def post(self,request,id):
        data=TaskModel.objects.get(id=id)
        form=TaskForm()
        if request.method == 'POST':
            updated_status = TaskModel.objects.get(id=id)
            updated_status.Status=request.POST['Status']
            updated_status.save()
            return redirect('home')
    
        context={'form':form,'data':data}
        return render(request,'TaskManagerApp/edittask.html',context)



# Class for viewing all task
class viewalltask(View):
    def get(self,request):
        data = TaskModel.objects.all()
        return render(request,'TaskManagerApp/viewtask.html',{'data':data})



# Adding client in Client Model
class addclient(View):
    def post(self,request):
        if request.method == 'POST':
            form=ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('addproject')
            
        messages.warning(request,'Something went Wrong')
        return redirect('home')
        


# Edit Project EndDate
class editproject(View):
    def get(self,request,id):
        data=ProjectModel.objects.get(id=id)
        form=ProjectForm()
        context={'form':form,'data':data}
        return render(request,'TaskManagerApp/editproject.html',context) 

    def post(self,request,id):
        data=ProjectModel.objects.get(id=id)
        form=ProjectForm()
        context={'form':form,'data':data}

        if request.method == 'POST':

# to show projects whose EndDate is more than Today
            Edate=request.POST['EndDate']
            end_date=datetime.strptime(Edate,'%m/%d/%Y')

            to_day=datetime.now().strftime('%m/%d/%Y')
            today=datetime.strptime(to_day,'%m/%d/%Y')

            if request.method == 'POST':

            # Calculated today and end date so that end should not be smaller or equal to today for a particular project
                if str(today)>str(end_date):
                    messages.warning(request,'End Date smaller than Today')
                    return render(request,'TaskManagerApp/editproject.html',context)
                
                elif str(today)==str(end_date):
                    messages.warning(request,'End Date and Today cannot be same ')
                    return render(request,'TaskManagerApp/editproject.html',context)
            
                else:
                    updated_status = ProjectModel.objects.get(id=id)
                    updated_status.EndDate=end_date
                    updated_status.save()
                    return redirect('home')

        return render(request,'TaskManagerApp/editproject.html',context)


# Class to show all Projects
class viewallproject(View):
    def get(self,request):
        data=ProjectModel.objects.all()

# Pagination for all projects
        data_paginator = Paginator(data,10)

        page_num= request.GET.get('page')

        page=data_paginator.get_page(page_num)
        return render(request,'TaskManagerApp/viewallproject.html',{'page':page})

