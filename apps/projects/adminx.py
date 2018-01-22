# -*- coding: utf-8 -*-
import xadmin
from .models import Projects, Missions, Stages

# list_display = []
# search_fields = []
# list_filter = []


class ProjectsAdmin(object):
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目名称")
    field = models.CharField(max_length=30, choices=PROJECT_FIELD, default="未设置", verbose_name="所属领域")
    status = models.CharField(max_length=30, choices=PROJECT_STATUS, default="未开始", verbose_name="项目状态")
    version = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目版本")
    progress = models.IntegerField(default=0, verbose_name="项目进度")
    desc = models.TextField(max_length=500, verbose_name="项目描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    list_display = ['name', 'user', 'field', 'status', 'version', 'progress', 'add_time']
    search_fields = ['name', 'field', 'status', 'version', 'progress']
    list_filter = ['name', 'field', 'status', 'version', 'progress', 'add_time']


class MissionsAdmin(object):
    """
    project = models.ForeignKey(Stages, null=True, blank=True, verbose_name="所属项目")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="阶段名")
    progress = models.IntegerField(default=0, verbose_name="任务进度")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    list_display = ['stage', 'user', 'name', 'progress', 'add_time']
    search_fields = ['stage__name', 'name']
    list_filter = ['stage__name', 'name']


class StagesAdmin(object):
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="阶段名")
    project = models.ForeignKey(Projects, null=True, blank=True, verbose_name="项目")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    list_display = ['name', 'project', 'add_time']
    search_fields = ['name', 'project__name']
    list_filter = ['name', 'project__name']


# class ProjectUsersAdmin(object):
#     list_display = ['user', 'project', 'add_time']
#     search_fields = ['user__username', 'project__name']
#     list_filter = ['user__username', 'project__name', 'add_time']


# class MissionUsersAdmin(object):
#     """
#     user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="成员")
#     mission = models.ForeignKey(Missions, null=True, blank=True, verbose_name="任务")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#     """
#     list_display = ['user', 'mission', 'add_time']
#     search_fields = ['user__username', 'mission__name']
#     list_filter = ['user__username', 'mission__name']


xadmin.site.register(Projects, ProjectsAdmin)
xadmin.site.register(Stages, StagesAdmin)
xadmin.site.register(Missions, MissionsAdmin)

# xadmin.site.register(ProjectUsers, ProjectUsersAdmin)
# xadmin.site.register(MissionUsers, MissionUsersAdmin)
