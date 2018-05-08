# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/19 上午12:06'

from django.conf.urls import url
from .views import FilmListView,VideoPlayView,AddComentsView,AddFavFilmView,AddScoreView,DelCommentView

urlpatterns =[
    url(r'^list/$', FilmListView.as_view(), name="film_list"),
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),
    url(r'^add_fav/$', AddFavFilmView.as_view(), name="add_fav"),
    url(r'^add_score/$', AddScoreView.as_view(), name="add_score"),
    url(r'^del_comment/$', DelCommentView.as_view(), name="del_comment"),
    # url(r'^home/(?P<reg_id>\d+)/$', RegHomeView.as_view(), name="reg_home"),
    # url(r'^film/(?P<reg_id>\d+)/$', RegFilmView.as_view(), name="reg_film"),
    # url(r'^director/(?P<reg_id>\d+)/$', RegDirectorView.as_view(), name="reg_director"),
]