from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
# Register your models here.

class ProjectAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'name', 'description', 'startdate', 'enddate']
    list_filter = ['user', 'name', 'description']

class DocumentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'project', 'doc_name']


class DepartmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['id', 'user', 'dep_name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Summary)




