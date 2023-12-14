import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from mgmt.models import Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(100000):
            created_at = timezone.now() - timedelta(days=random.randint(0, 365))
            end_date = created_at + timedelta(days=random.randint(1, 30))
            is_active = end_date > timezone.now()

            Project.objects.create(
                name=f'Dummy Project {_}',
                description=f'Dummy project description {_}',
                startdate=created_at,
                enddate=end_date,
                is_active=is_active,
            )

        projects_by_week = {}
        projects = Project.objects.all()

        for project in projects:
            week_number = project.startdate.strftime('%B_week_%U')
            projects_by_week[week_number] = projects_by_week.get(week_number, 0) + 1

        for week, count in projects_by_week.items():
            self.stdout.write(self.style.SUCCESS(f'{week}: {count}'))
