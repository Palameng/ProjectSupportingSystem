# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-14 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20170924_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='项目中的成员'),
        ),
    ]
