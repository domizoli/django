# Generated by Django 5.1.1 on 2024-10-01 16:46

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cv_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=80, verbose_name='name')),
                ('email', models.EmailField(default='john_doe@unknow.com', max_length=254, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('linkedin', models.URLField(verbose_name='www.linkedin.com')),
                ('address', models.CharField(default='', max_length=80)),
                ('profile', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='cv_user_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('title', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=50)),
                ('cv_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.cv_user')),
            ],
        ),
        migrations.CreateModel(
            name='cv_user_language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('level', models.DecimalField(decimal_places=0, max_digits=3)),
                ('cv_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.cv_user')),
            ],
        ),
        migrations.CreateModel(
            name='cv_user_work_expercience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('workPlace', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('jobTitle', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=150)),
                ('professionSkills', models.TextField(max_length=150)),
                ('cv_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.cv_user')),
            ],
        ),
    ]