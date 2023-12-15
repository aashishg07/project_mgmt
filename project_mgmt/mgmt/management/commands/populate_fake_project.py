import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from mgmt.models import Project, MyUser, Department
from faker import Faker


class Command(BaseCommand):
     def handle(self, *args, **kwargs):
        faker = Faker()
        faker.seed_instance(timezone.now().timestamp())
        total = kwargs.get("total", 10)
        user_id = kwargs.get("id", 1)

        created_at = timezone.now() - timedelta(days=random.randint(0, 365))
        end_date = created_at + timedelta(days=random.randint(1, 30))

        department_instance, created = Department.objects.get_or_create(id=1)
        project_bulk = []
        for _ in range(total):
            data = {
                "user": MyUser.objects.get(id=user_id),
                "name": faker.word(),
                "department": department_instance,
                "description": faker.text(),
                "startdate": created_at,
                "enddate": end_date,
            }
            project = Project(**data)
            project_bulk.append(project)
        Project.objects.bulk_create(project_bulk)


