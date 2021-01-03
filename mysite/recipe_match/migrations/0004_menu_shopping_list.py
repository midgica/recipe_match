# Generated by Django 3.1.4 on 2021-01-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_match', '0003_auto_20201225_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True, max_length=2000)),
                ('ingredients', models.ManyToManyField(to='recipe_match.Ingredient')),
            ],
        ),
    ]
