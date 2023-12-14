from .models import Project
from user.models import MyUser


class Summary:
    def get_total_users():
        return MyUser.objects.count()
    
    def get_total_projects():
        return Project.objects.count()