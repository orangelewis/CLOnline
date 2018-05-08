# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/7 下午5:30'
import xadmin

from .models import ContinentDict,Region,Director

class ContinentDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    model_icon = 'fa fa-university'

class RegionAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'continent', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums']
    readonly_filter = ['click_nums', 'fav_nums']
    style_fields = {"desc": "ueditor"}
    model_icon = 'fa fa-university'


class DirectorAdmin(object):
    list_display = ['reg', 'name']
    search_fields = [ 'name']
    list_filter = ['name']
    style_fields = {"desc": "ueditor"}
    model_icon = 'fa fa-user-md'
    relfield_style = 'fk-ajax'





xadmin.site.register(ContinentDict, ContinentDictAdmin)
xadmin.site.register(Region, RegionAdmin)
xadmin.site.register(Director, DirectorAdmin)