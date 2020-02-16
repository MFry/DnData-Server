from django.db import models

# Players and their characters
class Player(models.Model):
    name = models.CharField(max_length=100)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Character(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField()
    campaign = models.ForeignKey("Campaign", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
