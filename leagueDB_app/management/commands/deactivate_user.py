from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Deactivate user in the database'

    def handle(self, *args, **options):
        username = input('Please type the username of the user you want remove: ')
        try:
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            print('User is now deactivated in the database.')
        except User.DoesNotExist:
            print('Username not found')

