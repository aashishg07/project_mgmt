from celery import shared_task
from .models import Summary
from io import StringIO
from django.core.management import call_command

@shared_task
def update_summary():
    summaries = Summary.objects.all()
    for summary in summaries:
        summary.save()


@shared_task
def add_fake_project(total, id):
    stdout = StringIO()
    call_command("populate_fake_projects", total, id, stdout=stdout)