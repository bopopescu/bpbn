# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0030_character_sect'),
    ]

    operations = [
        migrations.AddField(
            model_name='vampire',
            name='clan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homeclan', to='domainmanager.Clan'),
        ),
    ]