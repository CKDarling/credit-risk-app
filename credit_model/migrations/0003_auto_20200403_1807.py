# Generated by Django 2.2.4 on 2020-04-03 18:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_model', '0002_auto_20200329_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='new_exist',
            field=models.PositiveIntegerField(choices=[('Existing Business', 'Existing Business'), ('New Business', 'New Business')], validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='loan',
            name='urban_rural',
            field=models.PositiveIntegerField(choices=[('Rural', 'Rural'), ('Undefined', 'Undefined'), ('Urban', 'Urban')], validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
