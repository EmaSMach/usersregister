# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-04 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20181204_0034'),
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
    ]