# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 09:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=datetime.datetime(2016, 8, 2, 9, 16, 44, 517199, tzinfo=utc), max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
