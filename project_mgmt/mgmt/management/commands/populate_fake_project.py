from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from mgmt.models import Project

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument("total", type=int, help="total: total number of projects")
        parser.add_argument("id", type=int, help="id: User id of the project")

    def handle(self, *args, **kwargs):
        faker = Faker()
        faker.seed_instance(timezone.now().timestamp())
        total = kwargs.get("total", 10)
        user_id = kwargs.get("id", 1)
        project_bulk = []
        for i in range(total):
            data = {
                "user": User.objects.get(id=user_id),
                "title": faker.word(),
                "description": faker.text(),
                "status": True if i % 2 == 0 else False,
                "deadline": timezone.now(),
            }
            project = Project(**data)
            project_bulk.append(project)
        Project.objects.bulk_create(project_bulk)
        self.stdout.write(
            self.style.SUCCESS(f"Successfull added total {total} projects")
        )