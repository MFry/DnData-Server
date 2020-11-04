from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.manager import Manager
from .campain import Campaign


class CharacterClassManager(Manager):
    def create_class(self, name: str, url: str):
        character_class = self.create(name=name, url=url)
        return character_class


class CharacterClass(models.Model):
    name = models.TextField(unique=True)
    url = models.URLField()

    objects = CharacterClassManager()


class CharacterSubclassManager(Manager):
    def create_class(self, name: str, url: str, character_class):
        character_class = self.create(
            name=name, url=url, character_class=character_class
        )
        return character_class


class CharacterSubclass(models.Model):
    name = models.TextField()
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    url = models.URLField()

    objects = CharacterSubclassManager()


class RaceManager(Manager):
    def create_race(self, name: str, url: str):
        race = self.create(name=name, url=url)
        return race


class Race(models.Model):
    name = models.TextField(unique=True)
    url = models.URLField()

    objects = RaceManager()


class CharacterSubrace(models.Model):
    name = models.TextField()
    url = models.URLField()


class Character(models.Model):
    name = models.TextField()
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    character_subClass = models.ForeignKey(CharacterSubclass, on_delete=models.CASCADE)
    character_subRace = models.ForeignKey(
        CharacterSubrace, blank=True, null=True, on_delete=models.CASCADE
    )
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    url = models.URLField()
