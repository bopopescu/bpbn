# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0125_auto_20160830_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='xpprize',
            field=models.IntegerField(default=0, help_text='Only use XP costs here for merits and flaws! All other XP costs are set in property types'),
        ),
        migrations.AlterField(
            model_name='propertytype',
            name='stattype',
            field=models.IntegerField(choices=[(1, 'Physical'), (2, 'Social'), (3, 'Mental'), (4, 'Talents'), (5, 'Skills'), (6, 'Knowledges'), (7, 'Backgrounds'), (8, 'Disciplines'), (9, 'Merits'), (10, 'Flaws'), (11, 'Rituals'), (12, 'Thaumaturgic Paths'), (13, 'Necromantic Paths'), (14, 'Influences')], default=4),
        ),
    ]
