# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-04 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import profiles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medias',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Medias',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[profiles.validators.validate_first_name])),
                ('last_name', models.CharField(max_length=100, validators=[profiles.validators.validate_last_name])),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=100, null=True, validators=[profiles.validators.validate_email])),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField()),
                ('timezone', models.CharField(blank=True, max_length=50, null=True, validators=[profiles.validators.validate_timezone])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Address')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Gender')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='medias',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.Users'),
        ),
    ]
