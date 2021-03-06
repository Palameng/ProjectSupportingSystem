# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from users.models import UserProfile
from projects.models import Projects
from weekreports.models import WeekReport
from .forms import NewProjectForm
# Create your views here.


class IndexView(View):
    # 进入系统后的首页
    def get(self, request):
        user = UserProfile.objects.get(username=request.user.username)

        if not user:
            raise Exception

        all_my_projects = user.projects_set.all()[:2]
        all_my_weekreports = WeekReport.objects.filter(user=user)

        # sum_of_project = Projects.objects.all().count()

        return render(request, 'main_panel.html', {
            "user": user,
            # "sum_of_project": sum_of_project,
            # "project_user_list": project_user_list,
            "all_my_projects": all_my_projects,
            "all_my_weekreports": all_my_weekreports,
        })


class FormTestView(View):
    # Form 测试
    def get(self, request):
        all_users = UserProfile.objects.all()
        new_project_form = NewProjectForm()
        return render(request, "formtest.html", {
            "new_project_form": new_project_form,
            "all_users": all_users,
        })
