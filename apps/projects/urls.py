# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import MyProjectsListView, CreateProjectStepOneView, ProjectDetailView, MissionDetailView, TestTreeView, MyMissionsListView
urlpatterns = [
    url(r'^ownlist/$', MyProjectsListView.as_view(), name='own_project_list'),
    url(r'^ownmissionslist/$', MyMissionsListView.as_view(), name='own_mission_list'),
    url(r'^add/$', CreateProjectStepOneView.as_view(), name='project_add'),
    url(r'^detail/(?P<project_id>\d+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^mission_detail/(?P<mission_id>\d+)/$', MissionDetailView.as_view(), name='project_mission_detail'),
    url(r'^tree/$', TestTreeView.as_view(), name='test_tree'),
]
