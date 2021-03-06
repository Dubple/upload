# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-10 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0002_auto_20161009_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='shared',
            field=models.ManyToManyField(blank=True, related_name='shared', to=settings.AUTH_USER_MODEL),
        ),
    ]
