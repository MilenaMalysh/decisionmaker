# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171124_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='leader',
            field=models.IntegerField(default=0),
        ),
    ]
