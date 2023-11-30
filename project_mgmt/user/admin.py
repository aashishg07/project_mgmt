from django.contrib import admin
from user.models import MyUser
from django import forms
from import_export.admin import ExportActionMixin

# Register your models here.


class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'name']


class UserAdmin(ExportActionMixin ,admin.ModelAdmin):
    list_display = ['email', 'name']
    form = UserForm

admin.site.register(MyUser, UserAdmin)
