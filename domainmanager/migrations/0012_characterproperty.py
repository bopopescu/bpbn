# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 20:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0011_auto_20160510_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='domainmanager.Character')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='domainmanager.Property')),
            ],
        ),
    ]
