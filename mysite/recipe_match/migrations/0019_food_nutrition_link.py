# Generated by Django 3.1.4 on 2021-01-09 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_match', '0018_auto_20210108_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='nutrition_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
