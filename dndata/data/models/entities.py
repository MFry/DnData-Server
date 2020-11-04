from django.db import models

from .players import Character


class Entities(models.Model):
    name = models.TextField()
    character = models.ForeignKey(Character, blank=True, null=True)


class Monsters(models.Model):
    name = models.TextField()
