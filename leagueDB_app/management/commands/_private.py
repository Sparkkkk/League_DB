# _private.py
from django.core.management.base import BaseCommand, CommandError


class SharedCommand(BaseCommand):

    def check_validity(self, color):
        return 0

