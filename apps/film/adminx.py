# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/7 下午5:30'
import xadmin

from .models import Film,FilmResource,Video,BannerFilm,BanWord
from region.models import Region



class FilmResourceInline(object):
    model = FilmResource
    extra = 0


class VideoInline(object):
    model = Video
    extra = 0

class FilmAdmin(object):
    list_display = ['name', 'desc', 'times']
    search_fields = ['name']
    list_filter = ['name', 'desc',  'times']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    list_editable = ['desc']
    exclude = ['fav_nums','score','score_nums']
    inlines = [ FilmResourceInline,VideoInline]
    style_fields = {"desc":"ueditor"}
    relfield_style = 'fk-ajax'
    import_excel = True

    def queryset(self):
        qs = super(FilmAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #在保存电影的时候统计国家的电影数
        obj = self.new_obj
        obj.save()
        if obj.film_reg is not None:
            film_reg = obj.film_reg
            film_reg.region_nums = Film.objects.filter(film_reg=film_reg).count()
            film_reg.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(FilmAdmin, self).post(request, args, kwargs)


class BannerFilmAdmin(object):
    list_display = ['name', 'desc', 'times']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'times']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [ FilmResourceInline]

    def queryset(self):
        qs = super(BannerFilmAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs





class VideoAdmin(object):
    list_display = ['film', 'name', 'add_time']
    search_fields = ['film', 'name']
    list_filter = ['film', 'name', 'add_time']
    model_icon = 'fa fa-film'


class FilmResourceAdmin(object):
    list_display = ['film', 'name', 'download', 'add_time']
    search_fields = ['film', 'name', 'download']
    list_filter = ['film', 'name', 'download', 'add_time']


class BanWordAdmin(object):
    list_display = ['ban_word','add_time']
    search_fields = ['ban_word']
    list_filter = ['ban_word']


xadmin.site.register(FilmResource, FilmResourceAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(BannerFilm, BannerFilmAdmin)
xadmin.site.register(Film, FilmAdmin)
xadmin.site.register(BanWord,BanWordAdmin)

