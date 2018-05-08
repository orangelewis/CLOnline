from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField

from django.db import models


# Create your models here.

#洲的信息
class ContinentDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"洲")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"洲"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#国家信息
class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名称")
    desc = models.TextField(verbose_name=u"描述")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"喜爱数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"logo", max_length=100)
    film_nums = models.IntegerField(default=0, verbose_name=u"电影数")
    continent=models.ForeignKey(ContinentDict,verbose_name=u"所属洲")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"国家地区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_dirctor_nums(self):
        # 获取导演数量
        return self.director_set.all().count()

    def get_film_nums(self):
        return self.film_set.all().count()



#导演
class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"名字")
    desc = UEditorField(verbose_name=u"导演描述",width=900, height=300, imagePath="reg/ueditor/",
                                         filePath="reg/ueditor/", default='')
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"喜爱数")
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    image = models.ImageField(default='', upload_to="director/%Y/%m", verbose_name=u"头像", max_length=100)
    reg = models.ForeignKey(Region, verbose_name=u"所属国家地区")
    add_time = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = u"导演"
        verbose_name_plural = verbose_name

    def get_fav_users(self):
        return self.userfavoritedirector_set.all()[0:5]

    def __str__(self):
        return self.name