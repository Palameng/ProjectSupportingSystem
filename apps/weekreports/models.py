from django.db import models
from users.models import UserProfile
from datetime import datetime
# Create your models here.


class WorkGroup(models.Model):
    """
    小组
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="小组名")

    class Meta:
        verbose_name = "小组"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class WeekReport(models.Model):
    """
    普通周报
    """
    topic = models.CharField(max_length=30, null=True, blank=True, verbose_name="标题")
    content = models.CharField(max_length=120, null=True, blank=True, verbose_name="内容")
    user = models.ForeignKey(UserProfile, null=True, blank=True, verbose_name="所属小组")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = "普通周报"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.topic
