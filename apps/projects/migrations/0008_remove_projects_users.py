# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-14 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20171014_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='users',
        ),
    ]
