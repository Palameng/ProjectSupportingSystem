# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import Projects, ProjectUsers, ProjectFirstCategory
# Create your views here.


class ListView(View):
    def get(self, request):
        all_projects = Projects.objects.all()
        users_to_projects = ProjectUsers.objects.all()
        return render(request, 'projects/project_list.html', {
            "all_projects": all_projects,
            "users_to_projects": users_to_projects,
        })


class AddView(View):
    def get(self, request):
        return render(request, 'projects/project_add.html', {

        })


class DetailView(View):
    def get(self, request, project_id):
        all_missions = ProjectFirstCategory.objects.filter(project__id=int(project_id))

        return render(request, 'projects/project_detail.html', {
            "all_missions": all_missions,
        })
