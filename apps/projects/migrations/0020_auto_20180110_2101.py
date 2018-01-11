# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-10 21:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0019_stages_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='missions',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='任务负责人'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='项目主要开发者'),
        ),
    ]