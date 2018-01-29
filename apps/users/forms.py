# -*- coding: utf-8 -*-
from django import forms


class NewProjectForm(forms.Form):
    """
    user = models.ManyToManyField(UserProfile, verbose_name="项目主要开发者")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目名称")
    field = models.CharField(max_length=30, choices=PROJECT_FIELD, default="未设置", verbose_name="项目类型")
    status = models.CharField(max_length=30, choices=PROJECT_STATUS, default="未开始", verbose_name="项目阶段")
    version = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目版本")
    progress = models.IntegerField(default=0, verbose_name="项目进度")
    desc = models.TextField(max_length=500, verbose_name="项目描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    project_name = forms.CharField(label='项目名称', max_length=5, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    project_type = forms.CharField(label='项目类型', required=True)
    project_detail = forms.CharField(label='项目类型', required=True)

