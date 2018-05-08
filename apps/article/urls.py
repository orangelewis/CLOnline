# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/31 下午11:33'


from django.conf.urls import url
from .views import Film_articleView,ArticleDetailView

urlpatterns =[
    url(r'^list/$', Film_articleView.as_view(), name="article_list"),
    url(r'^article/(?P<url_object_id>.*)/$', ArticleDetailView.as_view(), name="article_detail"),

]