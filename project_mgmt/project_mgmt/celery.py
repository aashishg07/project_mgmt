import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project_mgmt.settings')

app = Celery("mgmt")

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'update-summary-data-nightly': {
        'task': 'mgmt.tasks.update_summary',
        'schedule': crontab(hour=0, minute=0),
    },
    "add_fake_project_every_minute": {
        "task": "mgmt.tasks.populate_fake_project_data",
        "schedule": crontab(minute="*/1"),
        "args": (10, 1),
    },
}