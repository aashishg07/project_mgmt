# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Project
# # from user.models import MyUser

# @receiver(post_save, sender=Project)
# def change_project(sender, instance, created, **kwargs):
#     if created:
#         print("Project has been changed.", instance.name)