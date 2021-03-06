# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-28 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0058_remove_boon_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boonworkflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approvedbygm', models.BooleanField(default=False)),
                ('approvedbygm_note', models.TextField(default='Place for additional notes')),
                ('approvedbyslave', models.BooleanField(default=False)),
                ('approvedbyslave_note', models.TextField(default='Place for additional notes')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('boon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domainmanager.Boon')),
            ],
        ),
    ]
