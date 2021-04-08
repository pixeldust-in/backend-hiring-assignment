from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer,TaskSerializer
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination




def home(request):
    return render(request , 'home.html')


def login_attempt(request):
    return render(request , 'login.html')


class ProjectView(APIView):
    
    #authentication_class = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self , request):
        queryset = Project.objects.filter(client = request.user)
        serializer = ProjectSerializer(queryset, many=True)

        return Response(serializer.data)
    
    def post(self , request):
        response = {}
        response['status_code'] = 500
        response['message'] = 'Something went wrong'
        try:
            data_serializer = ProjectSerializer(data=request.data)
            if data_serializer.is_valid():
                data_serializer.save()
                response['status_code'] = 200
                response['message'] = 'project created successfully'
                response['data']  = data_serializer.data
            else:
                response['errors']  = data_serializer.errors
            print(data_serializer.errors)
        except Exception as e:
            print(e)
        
        return Response(response)
            
            
    def put(self , request, *args, **kwargs):
        response = {}
        response['status_code'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data.get('id') is None:
                response['message'] = 'id is required'
                raise Exception('id not found')
                
            
            queryset = Project.objects.get(id = data.get('id') )
            data_serializer = ProjectSerializer(queryset ,data =request.data , partial=True)
            if data_serializer.is_valid():
                data_serializer.save()
                response['status_code'] = 200
                response['message'] = 'project updated successfully'
                response['data']  = data_serializer.data
            else:
                response['errors']  = data_serializer.errors
         
            
        except Exception as e:
            print(e)
        return Response(response)
    

    def delete(self , request):
        response = {}
        response['status_code'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            project_obj = Project.objects.get(id = data.get('id'))
            
            project_obj.delete()
            response['status_code'] = 200
            response['message'] = 'project deleted successfully'
        except Exception as e:
            response['message'] = 'project with id does not exists successfully'
            
        return Response(response)
        
        
ProjectView = ProjectView.as_view()


class TaskView(APIView , LimitOffsetPagination):
    
    #authentication_class = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self , request):
        id = request.GET.get('project_id')
        
        if id is None:
            return Response({'error' : 'project_id is required'})

        queryset = Task.objects.filter(project__id = id , project__client=request.user)    
        page_number = request.GET.get('page_number', 1)
        page_size = self.request.query_params.get('page_size ', 10)
        paginator = Paginator(queryset , page_size)
        serializer = TaskSerializer(paginator.page(page_number), many=True , context={'request':request})
        
        return Response(serializer.data)
    
    def post(self , request):
        response = {}
        response['status_code'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            data_serializer = TaskSerializer(data=data)
            if data_serializer.is_valid():
                data_serializer.save()
                response['status_code'] = 200
                response['message'] = 'task created successfully'
                response['data']  = data_serializer.data
            else:
                response['errors']  = data_serializer.errors
            print(data_serializer.errors)
        except Exception as e:
            print(e)
        
        return Response(response)
            
            
    def put(self , request, *args, **kwargs):
        response = {}
        response['status_code'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            print(data)
            queryset = Task.objects.get(id = data.get('id'))
            data_serializer = TaskSerializer(queryset ,data=request.data , partial=True)
            if data_serializer.is_valid():
                data_serializer.save()
                response['status_code'] = 200
                response['message'] = 'task updated successfully'
                response['data']  = data_serializer.data
            else:
                response['errors']  = data_serializer.errors
            print(data_serializer.errors)
            
        except Exception as e:
            print(e)
            response['message'] = 'invalid task id'

        return Response(response)
    

    def delete(self , request):
        response = {}
        response['status_code'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            task_obj = Task.objects.get(id = data.get('id'))
            
            task_obj.delete()
            response['status_code'] = 200
            response['message'] = 'task deleted successfully'
        except Exception as e:
            response['message'] = 'task with id does not exists successfully'
            
        return Response(response)
        
        
TaskView = TaskView.as_view()





