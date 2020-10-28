from django.contrib import admin
from django.apps import apps
from .apps import DataConfig

models = apps.all_models[DataConfig.name]
admin.site.register(list(models.values()))