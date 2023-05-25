# Generated by Django 3.2.13 on 2023-05-24 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_genre_genre_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]