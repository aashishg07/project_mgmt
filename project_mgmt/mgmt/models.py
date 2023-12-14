from django.db import models
from user.models import MyUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class Department(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name
    

class Project(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    startdate = models.DateField(null=True)
    enddate = models.DateField()

    def __str__(self):
        return self.name
    
@receiver(post_save, sender = Project)
def update_project(instance, **kwargs):
    post_save.disconnect(update_project, sender=Project)
    instance.save()
    post_save.connect(update_project, sender=Project)
    print("\nChanged project successfully.\n")

    
class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=20)
    file = models.FileField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.doc_name
    

class Summary(models.Model):
    total_monthly_projects = models.PositiveBigIntegerField(null=True, blank=True)
    total_monthly_users = models.PositiveBigIntegerField(null=True, blank=True)
    total_monthly_files = models.PositiveBigIntegerField(null=True, blank=True)
    total_annual_projects = models.PositiveBigIntegerField(null=True, blank=True)
    total_annual_users = models.PositiveBigIntegerField(null=True, blank=True)
    total_annual_files = models.PositiveBigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
            now = timezone.now()

            self.total_monthly_projects = Project.objects.filter(startdate__month=now.month).count()
            self.total_monthly_users = MyUser.objects.filter(created_at__month=now.month).count()
            self.total_monthly_files = Document.objects.filter(created_at__month=now.month).count()

            self.total_annual_projects = Project.objects.filter(startdate__year=now.year).count()
            self.total_annual_users = MyUser.objects.filter(created_at__year=now.year).count()
            self.total_annual_files = Document.objects.filter(created_at__year=now.year).count()

            super().save(*args, **kwargs)