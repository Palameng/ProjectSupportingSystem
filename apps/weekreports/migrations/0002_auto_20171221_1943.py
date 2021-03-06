# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-21 19:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weekreports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekreport',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='weekreport',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
