from django.db import models
from django.db.models.deletion import CASCADE
from .campain import Campaign


class CharacterClassManager(models.Manager):
    def create_class(self, name: str, url: str):
        character_class = self.create(name=name, url=url)
        return character_class


class CharacterClass(models.Model):
    name = models.TextField(unique=True)
    url = models.URLField()

    objects = CharacterClassManager()


class CharacterSubclassManager(models.Manager):
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


class Race(models.Model):
    name = models.TextField(unique=True)
    url = models.URLField()


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
