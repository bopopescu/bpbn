# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0029_sect'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='sect',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Sect'),
        ),
    ]