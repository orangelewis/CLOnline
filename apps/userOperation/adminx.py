# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/7 下午5:30'
import xadmin

from .models import FilmComments,UserFavoriteDirector,UserFavoriteFilm,UserMessage,UserScore

class FilmCommentsAdmin(object):
    list_display = ['user', 'film', 'comments', 'add_time']
    search_fields = ['user', 'film', 'comments']
    list_filter = ['user', 'film', 'comments', 'add_time']
    model_icon = 'fa fa-comment'

class UserFavoriteDirectorAdmin(object):
    list_display = ['user', 'fav_id', 'director', 'add_time']
    search_fields = ['user', 'fav_id', 'director']
    list_filter = ['user', 'fav_id', 'director', 'add_time']
    model_icon = 'fa fa-heart'

class UserFavoriteFilmAdmin(object):
    list_display = ['user', 'fav_id', 'film', 'add_time']
    search_fields = ['user', 'fav_id', 'film']
    list_filter = ['user', 'fav_id', 'film', 'add_time']
    model_icon = 'fa fa-heart'


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-envelope-o'

class UserScoreAdmin(object):
    list_display = ['user','film', 'score',  'add_time']
    search_fields = ['user', 'film', ]
    list_filter = ['user','film', 'score',  'add_time']
    model_icon = 'fa fa-envelope-o'




xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavoriteFilm, UserFavoriteFilmAdmin)
xadmin.site.register(UserFavoriteDirector, UserFavoriteDirectorAdmin)
xadmin.site.register(FilmComments, FilmCommentsAdmin)
xadmin.site.register(UserScore,UserScoreAdmin)