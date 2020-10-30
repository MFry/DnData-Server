# Generated by Django 3.1.2 on 2020-10-30 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20201029_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_subRace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.charactersubrace'),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_subClass',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='data.charactersubclass'),
            preserve_default=False,
        ),
    ]
