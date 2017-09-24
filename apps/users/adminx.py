# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
__author__ = 'mengyuan'
__date__ = '2017/7/23 17:12'

import xadmin
from xadmin import views


# topic
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "后台系统"
    site_footer = "MengYuan"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
