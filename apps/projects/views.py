# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import Projects
# Create your views here.


class ListView(View):
    def get(self, request):
        all_projects = Projects.objects.all()
        return render(request, 'project_list.html', {
            "all_projects": all_projects,
        })
