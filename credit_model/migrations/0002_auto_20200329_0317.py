# Generated by Django 2.2.4 on 2020-03-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=600),
        ),
    ]
