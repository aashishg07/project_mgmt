from django.urls import path
from mgmt import views
from .views import DocumentList, ProjectFilterList

urlpatterns = [
    path('department/', views.departmentList, name="create_department"),
    path('department/<int:pk>/', views.deparmentDetail, name="detail_department"),
    path('project/', views.projectList, name="create_project"),
    path('project/<int:pk>/', views.projectDetail, name="detail_project"),
    path('documents/', views.documentList, name="create_documents"),
    path('documents/<int:pk>/', views.documentDetail, name="detail_documents"),
    path('document/filter/?', DocumentList.as_view(), name="filter_document"),
    # path('document/search/', DocumentList.as_view(), name="search_document"),
    path('project/filter/', ProjectFilterList.as_view(), name="filter_project_by_date")

]
