# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
__author__ = 'mengyuan'
__date__ = '2017/7/23 17:12'

import xadmin
from .models import WeekReport


class WeekReportAdmin(object):
    """
    topic = models.CharField(max_length=30, null=True, blank=True, verbose_name="标题")
    content = models.CharField(max_length=120, null=True, blank=True, verbose_name="内容")
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="作者")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    """
    list_display = ['user', 'topic', 'content', 'add_time']
    search_fields = ['user', 'topic', 'content']
    list_filter = ['user', 'topic', 'content', 'add_time']


xadmin.site.register(WeekReport, WeekReportAdmin)
