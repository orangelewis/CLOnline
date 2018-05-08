from datetime import datetime

from DjangoUeditor.models import UEditorField

from django.db import models
from region.models import Region,Director


# Create your models here.
# 电影
class Film(models.Model):
    film_reg = models.ForeignKey(Region, verbose_name=u"国家地区", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"电影名")
    desc = UEditorField(verbose_name=u"电影介绍",width=600, height=300, imagePath="film/ueditor/",
                                         filePath="film/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    director = models.ForeignKey(Director, verbose_name=u"导演", null=True, blank=True)
    times = models.IntegerField(default=0, verbose_name=u"播放时长(分钟数)")
    fav_nums = models.IntegerField(default=0, verbose_name=u'喜爱人数')
    image = models.ImageField(upload_to="film/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(default=u"大片", max_length=20, verbose_name=u"电影类别")


    #评分
    doubanId = models.IntegerField(default=0,verbose_name=u"豆瓣ID")
    score = models.FloatField(default=0,verbose_name=u"评分")
    score_nums = models.IntegerField (default=0,verbose_name=u"评论人数")


    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"电影"
        verbose_name_plural = verbose_name

    def get_fav_users(self):
        return self.userfavoritefilm_set.all()[:5]

    def __str__(self):
        return self.name


class BannerFilm(Film):
    class Meta:
        verbose_name = "轮播电影"
        verbose_name_plural = verbose_name
        proxy = True





class Video(models.Model):
    film = models.ForeignKey(Film, default=" ",verbose_name=u"电影")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    times = models.IntegerField(default=0, verbose_name=u"时长(分钟数)")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FilmResource(models.Model):
    film = models.ForeignKey(Film, verbose_name=u"电影")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"海报资源"
        verbose_name_plural = verbose_name

#敏感词语
class BanWord(models.Model):
    ban_word = models.CharField(max_length=100,verbose_name=u"敏感词")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"敏感词"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ban_word