# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-14 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='media/%Y/%m', verbose_name='头像'),
        ),
    ]
