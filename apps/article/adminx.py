# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/4 上午10:49'
import xadmin

from .models import Film_article,BannerArticle


class Film_articleAdmin(object):
    list_display = ['title', 'url', 'create_date','is_banner']
    search_fields = ['title', 'url', 'create_date']
    list_filter = ['title', 'url', 'create_date']
    list_editable = ["is_banner"]


class BannerArticleAdmin(object):
    list_display = ['title', 'url', 'create_date','is_banner']
    search_fields = ['title', 'url', 'create_date']
    list_filter = ['title', 'url', 'create_date']
    ordering = ['-click_nums']
    list_editable = ["is_banner"]
    readonly_fields = ['click_nums']
    def queryset(self):
        qs = super(BannerArticleAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs







xadmin.site.register(Film_article, Film_articleAdmin)
xadmin.site.register(BannerArticle, BannerArticleAdmin)

