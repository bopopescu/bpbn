# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0068_boon_hast_gm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boon',
            name='hast_gm',
        ),
    ]