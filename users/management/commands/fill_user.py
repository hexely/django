from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='1admin@mail.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('admin12345')
        user.save()

