from celery import shared_task
from .models import Summary
from django.core.management import call_command


@shared_task
def update_summary():
    summaries = Summary.objects.all()
    for summary in summaries:
        summary.save()


@shared_task
def populate_fake_project_data():
    call_command('populate_fake_project')
