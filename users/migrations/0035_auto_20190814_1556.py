# Generated by Django 2.2.3 on 2019-08-14 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_pg_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pg_account',
            name='accout_summary',
        ),
        migrations.RemoveField(
            model_name='pg_account',
            name='accout_summary_currency',
        ),
        migrations.RemoveField(
            model_name='pg_account',
            name='sum_credit',
        ),
        migrations.RemoveField(
            model_name='pg_account',
            name='sum_credit_currency',
        ),
        migrations.RemoveField(
            model_name='pg_account',
            name='sum_debit',
        ),
        migrations.RemoveField(
            model_name='pg_account',
            name='sum_debit_currency',
        ),
    ]
