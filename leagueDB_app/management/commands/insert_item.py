from django.core.management.base import BaseCommand, CommandError
from leagueDB_app.models import Item
import random

class Command(BaseCommand):
    help = 'Reset user table'

    def handle(self, *args, **options):
        reset_bool = input("input 1 to reset 0 otherwise: ")

        if reset_bool == '1':
            print(reset_bool)
            count = Item.objects.all().count()
            if count is not 0:
                Item.objects.all().delete()
            # add instance
            count = 10
            start_index = 1
            while start_index <= count:
                instance = Item(iid=start_index,
                         itemName='nickname' + str(start_index),
                         description=False if random.randint(0, 1) is 0 else True,
                         gold=random.randint(2000,5000))

                instance.save()
                start_index += 1
