# Generated by Django 2.2.3 on 2019-08-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20190815_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pgrp_account',
            name='sn',
        ),
        migrations.AddField(
            model_name='pgrp_account',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
