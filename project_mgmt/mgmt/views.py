from .models import Department, Project, Document
from .serializer import DepartmentSerializer, ProjectSerializer, DocumentSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import parser_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework import generics
from rest_framework import filters
from user.models import MyUser

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

class DocumentList(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend]
    #Search filter
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['doc_name']
    filterset_fields = ['created_at']

class UserStatsAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        month = self.request.query_params.get('month', None)
        queryset = Project.objects.filter(user__id = user_id, startdate__month = month)
        return queryset
    


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
    

# class DocumentList(generics.ListAPIView):
#     def get_queryset(self):
#         document = self.request.user
#         doc_found = Document.objects.filter(doc_name = document)
#         serializer = DocumentSerializer(doc_found)
#         return Response(serializer.data)

