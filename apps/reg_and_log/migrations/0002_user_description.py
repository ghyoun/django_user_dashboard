# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 23:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reg_and_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default=datetime.datetime(2016, 6, 21, 23, 39, 53, 447000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
