# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0027_auto_20160525_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodline',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='clan',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='rank',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
