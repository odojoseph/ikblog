# Generated by Django 2.2.3 on 2019-08-18 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_auto_20190818_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='min_evangelical',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterModelOptions(
            name='min_intercessory',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterModelOptions(
            name='min_leadership',
            options={'ordering': ['-date_elected']},
        ),
        migrations.AlterModelOptions(
            name='min_praiseworship',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterModelOptions(
            name='min_stewards',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterModelOptions(
            name='min_teaching',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterModelOptions(
            name='min_visitation',
            options={'ordering': ['-last_name']},
        ),
        migrations.AlterModelOptions(
            name='pgrp_account1',
            options={'ordering': ['-date']},
        ),
    ]