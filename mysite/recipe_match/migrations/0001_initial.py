# Generated by Django 3.1.4 on 2020-12-20 23:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plural', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=6)),
                ('notes', models.CharField(blank=True, max_length=100)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_match.food')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(max_length=30)),
                ('plural', models.CharField(blank=True, max_length=30)),
                ('full', models.CharField(blank=True, max_length=30)),
                ('full_plural', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tags', models.CharField(blank=True, max_length=200)),
                ('servings', models.PositiveSmallIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1)])),
                ('rating', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('instructions', models.TextField(max_length=5000)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_match.category')),
                ('ingredient_list', models.ManyToManyField(to='recipe_match.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_match.unit'),
        ),
    ]
