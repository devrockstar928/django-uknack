# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-02 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knacks', '0014_auto_20160701_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knack',
            name='thumbnail0',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='thumbnail1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='thumbnail2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='thumbnail3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='knack',
            name='thumbnail4',
            field=models.TextField(blank=True, null=True),
        ),
    ]