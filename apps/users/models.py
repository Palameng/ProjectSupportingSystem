# _*_ encoding:utf-8 _*
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    work_number = models.CharField(max_length=10, verbose_name=u"工号", default=u"")
    # birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    sex = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female")
    # address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username