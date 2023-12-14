from rest_framework import serializers
from .models import Department, Project, Document, Summary

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'user', 'dep_name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'department', 'user', 'startdate', 'enddate']

class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = ['id', 'project', 'doc_name', 'file', 'created_at']


class SummaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'
        

# class Summary(serializers.ModelSerializer):
#     class Meta:
#         model = Summary
#         fields = "__all__"
