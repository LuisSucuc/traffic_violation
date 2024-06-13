import os
from django.core.management.base import BaseCommand
from elements.models import Officer


class Command(BaseCommand):

    def handle(self, *args, **kwargs) -> None:
        '''
        Set the password for all users to the value of the environment variable DJANGO_SUPERUSER_PASSWORD
        '''
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        if not password:
            self.stdout.write(self.style.ERROR(
                'The environment variable DJANGO_SUPERUSER_PASSWORD is not set'))
            return

        users = Officer.objects.all()
        for user in users:
            user.set_password(password)
            user.save()

        self.stdout.write(self.style.SUCCESS(
            f'Successfully set the password for {len(users)} users'))
