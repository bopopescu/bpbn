# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0012_characterproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]