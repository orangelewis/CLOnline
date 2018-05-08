from django.db import models

from datetime import datetime

from users.models import UserProfile
from film.models import Film
from region.models import Director
# Create your models here.


class FilmComments(models.Model):
    "电影评论"
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    film = models.ForeignKey(Film, verbose_name=u"课程")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"电影评论"
        verbose_name_plural = verbose_name


class UserFavoriteFilm(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    film = models.ForeignKey(Film,verbose_name=u"电影")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户喜爱电影"
        verbose_name_plural = verbose_name


class UserFavoriteDirector(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    director = models.ForeignKey(Director,verbose_name=u"导演")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户喜爱导演"
        verbose_name_plural = verbose_name



class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserScore(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    film = models.ForeignKey(Film, verbose_name=u"电影")
    score = models.FloatField(default=0,verbose_name=u"评分")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户评分"
        verbose_name_plural = verbose_name



