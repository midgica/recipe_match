# Generated by Django 3.1.4 on 2021-01-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_match', '0007_auto_20210107_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='g_per_no_unit',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]