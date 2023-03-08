from rest_framework import serializers
from app.models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = ['id','name','client','start_date','end_date','tasks']




