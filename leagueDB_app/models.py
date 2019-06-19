from django.db import models

class LeagueDBModel(models.Model):
    col = models.CharField(max_length=200)

class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, unique=True)
    publicOrNot = models.BooleanField()

class Game(models.Model):
    gid = models.IntegerField(primary_key=True)
    blueWin = models.BooleanField()
    time = models.TimeField(auto_now=True)
    gameType = models.CharField(max_length=20)
    
class containsRecordPerMatch(models.Model):
    sid = models.IntegerField(primary_key=True)
    gid = models.IntegerField(unique=True)
    gid = models.ForeignKey(Game, on_delete=models.CASCADE)

class Champion(models.Model):
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    melee = models.BooleanField()

class asRecordPerMatch(models.Model):
    sid = models.IntegerField()
    cid = models.IntegerField()
    gold = models.IntegerField()
    kill = models.IntegerField()
    death = models.IntegerField()
    damage = models.IntegerField()
    damageTaken = models.IntegerField()
    cs = models.IntegerField()
    level = models.IntegerField()
    teamBlue = models.BooleanField()
    cid = models.ForeignKey(Champion, on_delete=models.CASCADE)

class Master(models.Model):
    cid = models.IntegerField(primary_key=True)
    uid = models.IntegerField(unique=True)
    point = models.IntegerField()
    topPlayer = models.IntegerField()
    cid = models.ForeignKey(Champion, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, related_name = 'user_id',on_delete=models.CASCADE)
    topPlayer = models.ForeignKey(User, related_name = 'top_player_id',on_delete=models.CASCADE)

class Item(models.Model):
    iid = models.IntegerField(primary_key=True)
    itemName = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=80, null=True)
    gold = models.IntegerField()

class Recommend(models.Model):
    cid = models.IntegerField(primary_key=True)
    iid = models.IntegerField(unique=True)
    cid = models.ForeignKey(Champion, on_delete=models.CASCADE)
    iid = models.ForeignKey(Item, on_delete=models.CASCADE)

class Object(models.Model):
    oid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=80, null=True)

class buyEvent(models.Model):
    eid = models.IntegerField(primary_key=True)
    iid = models.IntegerField(unique=True)
    time = models.TimeField(auto_now=True)
    iid = models.ForeignKey(Item, on_delete=models.CASCADE)

class getObjectEvent(models.Model):
    eid = models.IntegerField(primary_key=True)
    oid = models.IntegerField(unique=True)
    time = models.TimeField(auto_now=True)
    eid = models.ForeignKey(Object, on_delete=models.CASCADE)

class didObjectEvent(models.Model):
    eid = models.IntegerField(primary_key=True)
    oid = models.IntegerField(unique=True)
    time = models.TimeField(auto_now=True)
    oid = models.ForeignKey(asRecordPerMatch, on_delete=models.CASCADE)


class didKillEvent(models.Model):
    eid = models.IntegerField(primary_key=True)
    killerSid = models.IntegerField()
    victimSid = models.IntegerField(unique=True)
    time = models.TimeField(auto_now=True)
    victimSid = models.ForeignKey(asRecordPerMatch, on_delete=models.CASCADE)
