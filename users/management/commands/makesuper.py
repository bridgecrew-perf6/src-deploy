from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        qs = User.objects.filter(username='admin')
        if not qs.exists():
            User.objects.create_superuser(
                'admin',
                'admin@gmail.com',
                'test12345'
            )
