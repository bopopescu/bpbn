# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0015_auto_20160515_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='function',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.PoliticalFuntion'),
        ),
    ]
