from django.core.management.base import BaseCommand, CommandError
from leagueDB_app.models import asRecordPerMatch, Champion
import random

class Command(BaseCommand):
    help = 'Reset user table'

    def handle(self, *args, **options):
        reset_bool = input("input 1 to reset 0 otherwise: ")

        if reset_bool == '1':
            print(reset_bool)
            count = asRecordPerMatch.objects.all().count()
            if count is not 0:
                asRecordPerMatch.objects.all().delete()
            # add instance
            count = 20
            start_index = 1
            while start_index <= count:
                c = asRecordPerMatch(sid=start_index,
                                     cid=Champion.objects.all()[random.randint(0,9)],
                                     gold=random.randint(200,500),
                                     kill=random.randint(1,20),
                                     death=random.randint(1,20),
                                     damage=random.randint(3000,10000),
                                     damageTaken=random.randint(3000,10000),
                                     cs=random.randint(20,200),
                                     level=random.randint(1,18),
                                     teamBlue=True if random.randint(0,1) == 0 else False)
                c.save()
                start_index += 1
