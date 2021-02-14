# Generated by Django 2.2.3 on 2019-08-13 17:56

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_min_teaching_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_evangelical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('anouncer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('event_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_evangelical',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event_intercessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('anouncer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('event_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_intercessory',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event_leadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('anouncer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('event_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_leadership',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event_praiseworship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('anouncer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('event_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_praiseworship',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event_stewards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('anouncer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('event_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_stewards',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event_visitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('anouncer', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('event_img', models.ImageField(blank=True, upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event_visitation',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Min_Evangelical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField(default='1900-01-31')),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('next_of_kin', models.CharField(max_length=255)),
                ('next_of_kin_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('family_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_joined', models.DateField(default='1900-01-31')),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'min_evangelical',
            },
        ),
        migrations.CreateModel(
            name='Min_Intercessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField(default='1900-01-31')),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('next_of_kin', models.CharField(max_length=255)),
                ('next_of_kin_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('family_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_joined', models.DateField(default='1900-01-31')),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'min_intercessory',
            },
        ),
        migrations.CreateModel(
            name='Min_Leadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('position', models.CharField(max_length=200, null=True)),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('home_address', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_elected', models.DateField(default='1900-01-31')),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'min_leadership',
            },
        ),
        migrations.CreateModel(
            name='Min_Praiseworship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField(default='1900-01-31')),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('next_of_kin', models.CharField(max_length=255)),
                ('next_of_kin_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('family_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_joined', models.DateField(default='1900-01-31')),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'min_praiseworship',
            },
        ),
        migrations.CreateModel(
            name='Min_Stewards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField(default='1900-01-31')),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('next_of_kin', models.CharField(max_length=255)),
                ('next_of_kin_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('family_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_joined', models.DateField(default='1900-01-31')),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'min_stewards',
            },
        ),
        migrations.CreateModel(
            name='Min_Visitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('birthdate', models.DateField(default='1900-01-31')),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('next_of_kin', models.CharField(max_length=255)),
                ('next_of_kin_phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('family_name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('home_town', models.CharField(max_length=255)),
                ('lga_of_origin', models.CharField(max_length=255)),
                ('state_of_origin', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('ministry', models.CharField(choices=[('teach', 'Teaching'), ('pray', 'Intercessor'), ('evan', 'Evangelical'), ('visit', 'Visitation'), ('steward', 'Steward'), ('praise', 'Praise and Worship')], default='teach', max_length=255)),
                ('date_joined', models.DateField(default='1900-01-31')),
                ('passport', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'min_visitation',
            },
        ),
        migrations.AlterField(
            model_name='min_teaching',
            name='passport',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]