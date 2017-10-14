# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import ListView, AddView, DetailView
urlpatterns = [
    url(r'^list/$', ListView.as_view(), name='project_list'),
    url(r'^add/$', AddView.as_view(), name='project_add'),
    url(r'^detail/(?P<project_id>\d+)/$', DetailView.as_view(), name='project_detail'),
]
