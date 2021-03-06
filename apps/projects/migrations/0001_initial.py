# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-24 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='项目名称')),
                ('field', models.CharField(choices=[(1, '金融产品'), (2, '电信产品'), (3, '物联网相关')], default='未设置', max_length=30, verbose_name='所属领域')),
                ('status', models.CharField(choices=[(1, '立项阶段'), (2, '开发阶段'), (3, '测试阶段'), (4, '提交掩膜')], default='未开始', max_length=30, verbose_name='项目状态')),
                ('version', models.CharField(blank=True, max_length=30, null=True, verbose_name='项目版本')),
                ('progress', models.IntegerField(default=0, verbose_name='项目进度')),
                ('desc', models.TextField(max_length=500, verbose_name='项目描述')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
            },
        ),
    ]
