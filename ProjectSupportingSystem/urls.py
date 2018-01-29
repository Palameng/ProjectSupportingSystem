"""ProjectSupportingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from users.views import IndexView, FormTestView
from django.views.static import serve
from ProjectSupportingSystem.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    url('^$', IndexView.as_view(), name="index"),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^project/', include('projects.urls', namespace="project")),
    url(r'^weekreport/', include('weekreports.urls', namespace="weekreport")),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url('^formtest$', FormTestView.as_view(), name="formtest"),

]
