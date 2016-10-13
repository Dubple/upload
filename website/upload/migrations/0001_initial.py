# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-09 22:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=25)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2016, 10, 10, 10, 10, 10))),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', protocol='IPv4')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d')),
            ],
        ),
    ]
