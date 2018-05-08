# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/17 下午12:54'

from django.conf.urls import url, include
from .views import RegionView,RegHomeView,RegFilmView,RegDirectorView,DirectorListView,DirectorDetailView,AddFavDirectorView

urlpatterns =[
    url(r'^list/$', RegionView.as_view(), name="reg_list"),
    url(r'^home/(?P<reg_id>\d+)/$', RegHomeView.as_view(), name="reg_home"),
    url(r'^film/(?P<reg_id>\d+)/$', RegFilmView.as_view(), name="reg_film"),
    url(r'^director/(?P<reg_id>\d+)/$', RegDirectorView.as_view(), name="reg_director"),
    url(r'^dir_list/$', DirectorListView.as_view(), name="dir_list"),
    url(r'^director/detail/(?P<director_id>\d+)/$', DirectorDetailView.as_view(), name="director_detail"),
    url(r'^add_fav/$', AddFavDirectorView.as_view(), name="add_fav"),
]