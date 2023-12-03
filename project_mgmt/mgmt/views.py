from .models import Department, Project, Document
from .serializer import DepartmentSerializer, ProjectSerializer, DocumentSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import parser_classes
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

# class DepartmentView(generics.ListCreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

# class ProjectView(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class ProjectView(generics.ListAPIView):
#     queryset = Project.objects.get(pk=id)
#     serializer_class = ProjectSerializer


@api_view(['GET', 'POST'])
def departmentList(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET', 'DELETE'])
def deparmentDetail(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'msg': f'Id {pk} doesnot exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        department.delete()
        return Response({'msg': 'Deleted successfully!!!'}, status = status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def projectList(request):
    if request.method == 'GET':
        departments = Project.objects.all()
        serializer = ProjectSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def projectDetail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'msg': f'Id {pk} doesnot exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        project.delete()
        return Response({'msg': 'Deleted successfully!!!'}, status=status.HTTP_200_OK)


from rest_framework.parsers import MultiPartParser


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser])
def documentList(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'DELETE'])
def documentDetail(request, pk):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at']
    try:
        documents = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return Response({'msg': f'Id {pk} doesnot exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DocumentSerializer(documents)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        documents.delete()
        return Response({'msg': 'Deleted Successfully!!!'}, status=status.HTTP_200_OK)
    

