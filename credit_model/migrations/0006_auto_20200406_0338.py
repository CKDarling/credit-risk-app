# Generated by Django 2.2.4 on 2020-04-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_model', '0005_loan_prediction_prob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='prediction_prob',
            field=models.FloatField(),
        ),
    ]
