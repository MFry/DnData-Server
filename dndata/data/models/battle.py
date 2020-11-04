from django.db import models
from django.db.models.deletion import CASCADE


class Battles(models.Model):
    date = models.DateField()


class BattleEntries(models.Model):
    battle = models.ForeignKey(Battles, on_delete=CASCADE)


class Initiatives(models.Model):
    value = models.IntegerField()
