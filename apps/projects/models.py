from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.


class Projects(models.Model):

    PROJECT_FIELD = (
        ('1', "金融产品"),
        ('2', "电信产品"),
        ('3', "物联网相关"),
    )

    PROJECT_STATUS = (
        ('1', "立项阶段"),
        ('2', "开发阶段"),
        ('3', "测试阶段"),
        ('4', "结项"),
    )

    user = models.ManyToManyField(UserProfile, verbose_name="项目主要开发者")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目名称")
    field = models.CharField(max_length=30, choices=PROJECT_FIELD, default="未设置", verbose_name="项目类型")
    status = models.CharField(max_length=30, choices=PROJECT_STATUS, default="未开始", verbose_name="项目阶段")
    version = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目版本")
    progress = models.IntegerField(default=0, verbose_name="项目进度")
    desc = models.TextField(max_length=500, verbose_name="项目描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_this_project_all_staffs(self):
        return ",".join([user.username for user in self.user.all()])

    def set_progress(self):
        all_stages = self.stages_set.all()
        # 计算当前项目的进度值, 一个平均权重的计算法
        self.progress = 0
        for stage in all_stages:
            self.progress += stage.progress * (1/all_stages.count())


class Stages(models.Model):
    """
    项目-子阶段
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="阶段名")
    project = models.ForeignKey(Projects, null=True, blank=True, verbose_name="项目")
    progress = models.IntegerField(default=0, verbose_name="阶段进度")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "阶段"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.project.name + ':' + self.name)

    def get_all_missions(self):
        return self.missions_set.all()

    def get_progress(self):
        all_missions = self.missions_set.all()
        # 计算当前阶段的进度值, 一个平均权重的计算法
        self.progress = 0
        for mission in all_missions:
            self.progress += mission.progress * (1/all_missions.count())


class Missions(models.Model):
    """
    项目-子阶段-子任务
    """
    user = models.ManyToManyField(UserProfile, verbose_name="任务负责人")
    stage = models.ForeignKey(Stages, null=True, blank=True, verbose_name="所属阶段")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="任务名")
    progress = models.IntegerField(default=0, verbose_name="任务进度")
    content = models.TextField(verbose_name="任务详细", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "子任务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.stage.project.name + ':' + self.name)


# class ProjectUsers(models.Model):
#     """
#     项目成员关联表
#     """
#     user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="成员")
#     project = models.ForeignKey(Projects, null=True, blank=True, verbose_name="项目")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#
#     class Meta:
#         verbose_name = "项目成员关联表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.id)


# class MissionUsers(models.Model):
#     """
#     任务成员关联表
#     """
#     user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="成员")
#     mission = models.ForeignKey(Missions, null=True, blank=True, verbose_name="任务")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#
#     class Meta:
#         verbose_name = "任务成员关联表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.id)
