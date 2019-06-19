from django.db import models

class LeagueDBModel(models.Model):
    col = models.CharField(max_length=200)