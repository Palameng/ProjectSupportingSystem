# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import Projects, Missions, Stages
from .forms import AddProjectForm
from users.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
# Create your views here.


class MyProjectsListView(View):
    def get(self, request):
        all_projects = Projects.objects.all()
        # users_to_projects = ProjectUsers.objects.all()
        return render(request, 'projects/project_list.html', {
            "all_projects": all_projects,
            # "users_to_projects": users_to_projects,
        })


class AddView(View):
    """
    增加项目
    """
    def get(self, request):

        all_users = UserProfile.objects.all()

        return render(request, 'projects/create_project.html', {
            "all_users": all_users,
        })

    def post(self, request):
        project_add_form = AddProjectForm(request.POST)
        if project_add_form.is_valid():
            project_name = request.POST.get("projectName", "")
            project_type = request.POST.get("projectType", "")
            project_stuffs = request.POST.getlist("projectStuffs", "")
            project_detail = request.POST.get("projectDetail", "")

            new_project = Projects()
            new_project.name = project_name

            if project_type == "金融产品":
                new_project.field = '1'
            elif project_type == "电信产品":
                new_project.field = '2'
            elif project_type == "物联网相关":
                new_project.field = '3'

            new_project.status = '1'
            new_project.version = '0'
            new_project.progress = 0
            new_project.desc = project_detail
            new_project.add_time = datetime.now()

            new_project.save()

        return HttpResponseRedirect(reverse("index"))


class ProjectDetailView(View):
    """
    获取项目详情
    """
    def get(self, request, project_id):
        all_stages = Stages.objects.filter(project__id=int(project_id))
        current_project = Projects.objects.get(id=int(project_id))
        return render(request, 'projects/project_detail.html', {
            "all_stages": all_stages,
            "current_project": current_project,
        })


class MissionDetailView(View):
    """
    获取任务详情
    """
    def get(self, request, mission_id):
        current_mission = Missions.objects.get(id=int(mission_id))
        # current_mission_all_staffs = MissionUsers.objects.filter(id=int(mission_id))
        return render(request, "projects/project_mission_detail.html", {
            "current_mission": current_mission,
            # "current_mission_all_staffs": current_mission_all_staffs,
        })
