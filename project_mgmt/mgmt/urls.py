from django.urls import path
from mgmt import views

urlpatterns = [
    path('department/', views.departmentList, name="create_department"),
    path('department/<int:pk>/', views.deparmentDetail, name="detail_department"),
    path('project/', views.projectList, name="create_project"),
    path('project/<int:pk>/', views.projectDetail, name="detail_project"),
    path('documents/', views.documentList, name="create_documents"),
    path('documents/<int:pk>/', views.documentDetail, name="detail_documents")
]
