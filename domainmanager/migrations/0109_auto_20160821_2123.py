# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0108_auto_20160821_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_domain', to='domainmanager.Domain'),
        ),
    ]