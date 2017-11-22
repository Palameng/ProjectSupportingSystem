# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import Projects, ProjectUsers, Missions, Stages, MissionUsers
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
    """
    增加项目
    """
    def get(self, request):
        return render(request, 'projects/project_add.html', {

        })


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
        current_mission_all_staffs = MissionUsers.objects.filter(id=int(mission_id))
        return render(request, "projects/project_mission_detail.html", {
            "current_mission": current_mission,
            "current_mission_all_staffs": current_mission_all_staffs,
        })
