# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 14:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20160520_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='poster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_poster', to=settings.AUTH_USER_MODEL),
        ),
    ]
