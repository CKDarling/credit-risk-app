# Generated by Django 2.2.4 on 2020-04-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_model', '0003_auto_20200403_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='new_exist',
            field=models.CharField(choices=[('Existing Business', 'Existing Business'), ('New Business', 'New Business')], max_length=60),
        ),
        migrations.AlterField(
            model_name='loan',
            name='urban_rural',
            field=models.CharField(choices=[('Rural', 'Rural'), ('Undefined', 'Undefined'), ('Urban', 'Urban')], max_length=60),
        ),
    ]
