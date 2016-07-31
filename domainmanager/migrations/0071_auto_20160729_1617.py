# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 14:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0070_boon_hash_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactershopping',
            name='approvedbygm',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default=1, max_length=100, no_check_for_status=True),
        ),
        migrations.AddField(
            model_name='charactershopping',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 29, 14, 17, 14, 182069, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charactershopping',
            name='hash_gm',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='charactershopping',
            name='newproperty',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='charactershopping',
            name='newpropertytype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.PropertyType'),
        ),
        migrations.AddField(
            model_name='charactershopping',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Property'),
        ),
        migrations.AddField(
            model_name='charactershopping',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 29, 14, 17, 19, 471979, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='initatcharactercreation',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default=2, max_length=100, no_check_for_status=True),
        ),
    ]