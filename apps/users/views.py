# _*_ encoding:utf-8 _*
from django.shortcuts import render
from django.views.generic import View
from .models import UserProfile

# Create your views here.


class IndexView(View):
    def get(self, request):
        user = UserProfile.objects.get(username='mengyuan')
        return render(request, 'index.html', {
            "user": user,
        })
