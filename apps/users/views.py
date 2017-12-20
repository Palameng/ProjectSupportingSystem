# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import UserProfile
from projects.models import Projects, ProjectUsers
# Create your views here.


class IndexView(View):
    # 进入系统后的首页
    def get(self, request):
        user = UserProfile.objects.get(username=request.user.username)

        if not user:
            raise Exception

        project_user_list = ProjectUsers.objects.filter(user=user)

        # sum_of_project = Projects.objects.all().count()

        return render(request, 'main_panel.html', {
            "user": user,
            # "sum_of_project": sum_of_project,
            "project_user_list": project_user_list,
        })
