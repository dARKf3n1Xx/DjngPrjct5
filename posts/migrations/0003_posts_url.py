# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170208_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='url',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
