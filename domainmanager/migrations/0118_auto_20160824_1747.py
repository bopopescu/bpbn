# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 15:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import domainmanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('domainmanager', '0117_auto_20160824_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='agecategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=domainmanager.models.set_upload_directory_path),
        ),
        migrations.AddField(
            model_name='politicalfuntion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=domainmanager.models.set_upload_directory_path),
        ),
        migrations.AlterField(
            model_name='character',
            name='hasvisions',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No'), (3, 'Active'), (4, 'Passive')], default=2, help_text='Has the character visions?', verbose_name='Visions'),
        ),
        migrations.AlterField(
            model_name='character',
            name='schrecknetlevel',
            field=models.IntegerField(default=0, help_text='What is the Schrecknet level of the character?', validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)], verbose_name='Schrecknet level'),
        ),
    ]
