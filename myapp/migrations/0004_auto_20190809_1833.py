# Generated by Django 2.2.3 on 2019-08-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_serviceteam_teaching'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='debit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='tellerNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='amount_paid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='serviceteam',
            name='tel',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='noktel',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
