from django.db import models

class Campaign(models.Model):
    name = models.TextField()
    url = models.URLField()
