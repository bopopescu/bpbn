# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0086_auto_20160803_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='domain',
            field=models.ManyToManyField(to='domainmanager.Domain'),
        ),
    ]
