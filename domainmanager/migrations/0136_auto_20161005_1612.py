# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0135_charactersecret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='description',
            field=models.TextField(),
        ),
    ]