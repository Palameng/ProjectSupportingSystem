from django.db import models
from datetime import datetime
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
        ('4', "提交掩膜"),
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目名称")
    field = models.CharField(max_length=30, choices=PROJECT_FIELD, default="未设置", verbose_name="所属领域")
    status = models.CharField(max_length=30, choices=PROJECT_STATUS, default="未开始", verbose_name="项目状态")
    version = models.CharField(max_length=30, null=True, blank=True, verbose_name="项目版本")
    progress = models.IntegerField(default=0, verbose_name="项目进度")
    desc = models.TextField(max_length=500, verbose_name="项目描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
