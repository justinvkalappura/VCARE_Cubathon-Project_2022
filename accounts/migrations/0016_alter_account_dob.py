# Generated by Django 4.0.4 on 2022-05-23 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_account_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 1, 45, 52, 200981)),
        ),
    ]