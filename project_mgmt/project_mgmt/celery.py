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
    "add_fake_project_every_3_minute": {
        "task": "mgmt.tasks.add_fake_project",
        "schedule": crontab(minute="*/3"),
        "args": (10, 1),
    },
}