from django.core.management.base import BaseCommand, CommandError
from leagueDB_app.models import User


class Command(BaseCommand):
    help = 'Reset user table'

    def handle(self, *args, **options):
        reset_bool = input("input 1 to reset 0 otherwise: ")

        if reset_bool == '1':
            print(reset_bool)
            count = User.objects.all().count()
            if count is not 0:
                User.objects.all().delete()
            # add instance
            count = 10
            start_index = 1
            while start_index <= count:
                user = User(uid=start_index,
                            password='123',
                            nickname='nickname' + str(start_index),
                            publicOrNot=False)
                user.save()
                start_index += 1
