# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import ListView
urlpatterns = [
    url(r'^list/$', ListView.as_view(), name='project_list'),
]
