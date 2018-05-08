from DjangoUeditor.models import UEditorField
from datetime import datetime

from django.db import models

# Create your models here.

class Film_article(models.Model):
    url_object_id = models.CharField(max_length=50,verbose_name=u"url地址ID",primary_key = True)
    url = models.CharField(max_length=300, default="", verbose_name=u"url地址")
    click_nums = models.IntegerField(default=1, verbose_name=u"点击数")
    title = models.CharField(max_length=200, verbose_name=u"标题")
    front_image_url = models.CharField(max_length=300, default="", verbose_name=u"图片地址")
    front_image_name = models.CharField(max_length=300, default="", verbose_name=u"图片名字")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    article = UEditorField(verbose_name=u"文章",width=600, height=300, imagePath="article/ueditor/",
                                         filePath="article/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BannerArticle(Film_article):
    class Meta:
        verbose_name = "轮播文章"
        verbose_name_plural = verbose_name
        proxy = True