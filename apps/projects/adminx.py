# -*- coding: utf-8 -*-
import xadmin
from .models import Projects

# list_display = []
# search_fields = []
# list_filter = []


class ProjectsAdmin(object):
    list_display = ['name', 'field', 'status', 'version', 'progress', 'add_time']
    search_fields = ['name', 'field', 'status', 'version', 'progress']
    list_filter = ['name', 'field', 'status', 'version', 'progress', 'add_time']


xadmin.site.register(Projects, ProjectsAdmin)
