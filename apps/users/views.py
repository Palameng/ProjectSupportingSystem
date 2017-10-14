# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import UserProfile
from projects.models import Projects
# Create your views here.


class IndexView(View):
    def get(self, request):
        user = UserProfile.objects.get(username='admin')

        sum_of_project = Projects.objects.all().count()

        return render(request, 'index.html', {
            "user": user,
            "sum_of_project": sum_of_project
        })
