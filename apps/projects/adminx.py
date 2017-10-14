# -*- coding: utf-8 -*-
import xadmin
from .models import Projects, ProjectUsers, ProjectFirstCategory

# list_display = []
# search_fields = []
# list_filter = []


class ProjectsAdmin(object):
    list_display = ['name', 'field', 'status', 'version', 'progress', 'add_time']
    search_fields = ['name', 'field', 'status', 'version', 'progress']
    list_filter = ['name', 'field', 'status', 'version', 'progress', 'add_time']


class ProjectUsersAdmin(object):
    list_display = ['user', 'project', 'add_time']
    search_fields = ['user__username', 'project__name']
    list_filter = ['user__username', 'project__name', 'add_time']


class ProjectFirstCategoryAdmin(object):
    list_display = ['project', 'user', 'add_time', 'progress']
    search_fields = ['user__username', 'project__name']
    list_filter = ['user__username', 'project__name', 'progress', 'add_time']


xadmin.site.register(Projects, ProjectsAdmin)
xadmin.site.register(ProjectUsers, ProjectUsersAdmin)
xadmin.site.register(ProjectFirstCategory, ProjectFirstCategoryAdmin)
