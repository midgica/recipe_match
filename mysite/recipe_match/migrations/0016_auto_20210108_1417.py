# Generated by Django 3.1.4 on 2021-01-08 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_match', '0015_auto_20210108_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='shopping_list_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_match.unit'),
        ),
    ]
