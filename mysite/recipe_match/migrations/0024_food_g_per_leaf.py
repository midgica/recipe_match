# Generated by Django 3.1.4 on 2021-01-30 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_match', '0023_auto_20210125_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='g_per_leaf',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]