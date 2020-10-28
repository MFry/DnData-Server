from django.db import models
from django.db.models.deletion import CASCADE


class CharacterClass(models.Model):
    name = models.TextField()
    url = models.URLField()


class CharacterSubclass(models.Model):
    subClass = models.TextField()
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    url = models.URLField()


class Race(models.Model):
    name = models.TextField()
    url = models.URLField()


class CharacterRace(models.Model):
    name = models.TextField()
    url = models.URLField()


class CharacterSubrace(models.Model):
    name = models.TextField()
    url = models.URLField()


class Campaign(models.Model):
    name = models.TextField()
    url = models.URLField()


class Character(models.Model):
    name = models.TextField()
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    character_subClass = models.ForeignKey(CharacterSubclass, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    url = models.URLField()
