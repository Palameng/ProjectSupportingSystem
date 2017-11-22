# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import ListView, AddView, ProjectDetailView, MissionDetailView
urlpatterns = [
    url(r'^list/$', ListView.as_view(), name='project_list'),
    url(r'^add/$', AddView.as_view(), name='project_add'),
    url(r'^detail/(?P<project_id>\d+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^mission_detail/(?P<mission_id>\d+)/$', MissionDetailView.as_view(), name='project_mission_detail'),
]
