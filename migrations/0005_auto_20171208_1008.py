# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-08 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samehadago', '0004_auto_20171207_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='source',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='when',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
