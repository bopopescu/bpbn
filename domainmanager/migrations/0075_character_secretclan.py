# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-31 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0074_clan_standardclan'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='secretclan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secretclan', to='domainmanager.Clan'),
        ),
    ]
