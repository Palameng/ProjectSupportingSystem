# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import Projects, Missions, Stages
from .forms import AddProjectForm
from users.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
# Create your views here.


class MyProjectsListView(View):
    """
    个人参与的所有项目
    """
    def get(self, request):
        user = request.user
        all_my_projects = user.projects_set.all()

        # 对所有A进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 第二个参数代表每一页显示的个数
        p = Paginator(all_my_projects, 2, request=request)
        all_my_projects = p.page(page)

        # users_to_projects = ProjectUsers.objects.all()
        return render(request, 'projects/own_all_project.html', {
            "all_my_projects": all_my_projects,
            # "users_to_projects": users_to_projects,
        })


class MyMissionsListView(View):
    """
    个人参与的所有任务
    """
    def get(self, request):
        user = request.user
        all_my_missions = user.missions_set.all()

        # 对所有A进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 第二个参数代表每一页显示的个数
        p = Paginator(all_my_missions, 3, request=request)
        all_my_missions = p.page(page)

        # users_to_projects = ProjectUsers.objects.all()
        return render(request, 'projects/own_all_missions.html', {
            "all_my_missions": all_my_missions,
            # "users_to_projects": users_to_projects,
        })


class CreateProjectStepOneView(View):
    """
    增加项目第一步
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

            new_project = Projects.objects.create()
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

            # 添加ManytoMany关系
            for stuff_name in project_stuffs:
                new_project.user.add(UserProfile.objects.get(username=stuff_name))

            new_project.save()

        return HttpResponseRedirect(reverse("index"))


class ProjectDetailView(View):
    """
    获取项目详情
    """
    def get(self, request, project_id):
        current_project = Projects.objects.get(id=int(project_id))

        all_stages = current_project.stages_set.all()

        # 获取当前项目下每一个阶段的进度值
        for stage in all_stages:
            stage.get_progress()
            stage.save()

        # 获取当前项目的进度值
        current_project.progress = 0
        current_project.set_progress()
        current_project.save()

        return render(request, 'projects/detail_project.html', {
            "all_stages": all_stages,
            "current_project": current_project,
        })


class MissionDetailView(View):
    """
    任务详情和保存
    """
    def get(self, request, mission_id):
        """
        获取任务详情
        :param request:
        :param mission_id:
        :return:
        """
        current_mission = Missions.objects.get(id=int(mission_id))
        return render(request, "projects/detail_mission.html", {
            "current_mission": current_mission,
        })

    def post(self, request):
        """
        保存更改
        :param request:
        :return:
        """
        return render(request, "projects/detail_mission.html", {

        })


class CreateProjectStepTwoView(View):
    """
    填写创建项目的基础信息后初始化项目阶段和任务细节
    """
    pass


class TestTreeView(View):
    def get(self, request):
        return render(request, 'projects/fullcalendar.html', {

        })

