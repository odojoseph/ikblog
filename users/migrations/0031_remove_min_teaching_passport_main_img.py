# Generated by Django 2.2.3 on 2019-08-13 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20190813_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='min_teaching',
            name='passport_main_Img',
        ),
    ]
