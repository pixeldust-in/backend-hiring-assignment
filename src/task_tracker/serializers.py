from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if len(data['project_name']) >  1000:
            raise serializers.ValidationError("project_name cannot exceed 1000 chars")
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("start_date cannot be greator than end_date")     
        return data
    
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']
    

class TaskSerializer(serializers.ModelSerializer):
    #project = ProjectSerializer( many=True,read_only=True )
    project = serializers.ReadOnlyField( source="project.project_name",read_only=True)
    def validate(self, data):
        if len(data['task_name']) > 1000:
            raise serializers.ValidationError("task_name cannot exceed 1000 chars")

        return data
    
    class Meta:
        model = Task
        exclude = ['created_at', 'updated_at']