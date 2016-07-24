# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 19:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0018_auto_20160515_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterdiscipline',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]