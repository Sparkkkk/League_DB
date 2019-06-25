from django.core.management.base import BaseCommand, CommandError
from leagueDB_app.models import Champion
import random

class Command(BaseCommand):
    help = 'Reset user table'

    def handle(self, *args, **options):
        reset_bool = input("input 1 to reset 0 otherwise: ")

        if reset_bool == '1':
            print(reset_bool)
            count = Champion.objects.all().count()
            if count is not 0:
                Champion.objects.all().delete()
            # add instance
            count = 10
            start_index = 1
            while start_index <= count:
                c = Champion(cid=start_index,
                             name='champion_name' + str(start_index),
                             melee=False if random.randint(0, 1) is 0 else True)
                c.save()
                start_index += 1
