# Generated by Django 2.2.3 on 2019-08-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20190815_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgrp_account',
            name='sn',
            field=models.AutoField(default='0000000', editable=False, primary_key=True, serialize=False),
        ),
    ]