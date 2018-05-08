from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
from .models import ContinentDict,Region,Director
from userOperation.models import UserFavoriteFilm,UserFavoriteDirector
from film.models import Film



class RegionView(View):
    #国家
    def get(self,request):
        all_regs = Region.objects.all()

        all_continent = ContinentDict.objects.all()

        #搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_regs = all_regs.filter(Q(name__icontains=search_keywords))

        # 取出筛选城市
        continent_id = request.GET.get('continent', "")
        if continent_id:
            all_regs = all_regs.filter(continent_id=int(continent_id))

        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
           all_regs = all_regs.filter(category=category)

        sort = request.GET.get('sort', "")
        if sort:
            all_regs = all_regs.order_by("-film_nums")

        reg_nums = all_regs.count()

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_regs,3 ,request=request)

        regs = p.page(page)
        return render(request, "region_list.html", {
            "all_regs":regs,
            "all_continent":all_continent,
            "reg_nums":reg_nums,
            "continent_id":continent_id,
            "category":category,
            "sort":sort
        })

class RegHomeView(View):
    #首页
    def get(self,request,reg_id):
        current_page = "home"
        film_reg = Region.objects.get(id = int(reg_id))
        film_reg.click_nums += 1
        film_reg.save()
        all_film = film_reg.film_set.all()[:3]
        all_director = film_reg.director_set.all()[:3]
        return render(request,'reg-detail-homepage.html',{
            'all_film':all_film,
            'all_director':all_director,
            'film_reg':film_reg,
            'current_page':current_page,

        })

class RegFilmView(View):
    """
    电影列表页
    """
    def get(self,request,reg_id):
        current_page = "film"
        film_reg = Region.objects.get(id=int(reg_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavoriteFilm.objects.filter(user=request.user, fav_id=film_reg.id):
                has_fav = True
        all_films = film_reg.film_set.all()
        return render(request, 'reg-detail-film.html', {
            'all_films': all_films,
            'film_reg': film_reg,
            'current_page': current_page,
            'has_fav': has_fav
        })

class RegDirectorView(View):
    """
    导演列表页
    """

    def get(self, request, reg_id):
        current_page = "director"
        film_reg = Region.objects.get(id=int(reg_id))

        all_directors = film_reg.director_set.all()
        return render(request, 'reg-detail-directors.html', {
            'all_directors': all_directors,
            'film_reg': film_reg,
            'current_page': current_page,


        })


class DirectorListView(View):
    """
    课程讲师列表页
    """
    def get(self, request):
        all_directors = Director.objects.all()
        dir_nums = all_directors.count()

        #课程讲师搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_directors = all_directors.filter(Q(name__icontains=search_keywords))

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_directors = all_directors.order_by("-click_nums")

        sorted_director = Director.objects.all().order_by("-click_nums")[:5]

        #对讲师进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_directors, 5, request=request)

        directors = p.page(page)

        return render(request, "directors-list.html", {
            "all_directors":directors,
            "sorted_director":sorted_director,
            "sort":sort,
            "dir_nums":dir_nums
        })


class DirectorDetailView(View):
    def get(self, request, director_id):
        director = Director.objects.get(id=int(director_id))
        director.click_nums += 1
        director.save()
        all_films = Film.objects.filter(director=director)

        has_director_faved = False
        if request.user.is_authenticated():
            if UserFavoriteDirector.objects.filter(user=request.user, fav_id=director.id):
                has_director_faved = True



        #导演排行
        sorted_director = Director.objects.all().order_by("-click_nums")[:3]
        return render(request, "directors-detail.html", {
            "director":director,
            "all_films":all_films,
            "sorted_director":sorted_director,
            "has_director_faved": has_director_faved,
        })


class AddFavDirectorView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)


        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavoriteDirector.objects.filter(user=request.user, fav_id=int(fav_id))
        if exist_records:
            #如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            director = Director.objects.get(id=int(fav_id))
            director.fav_nums -= 1
            if director.fav_nums < 0:
                director.fav_nums = 0
            director.save()
            return HttpResponse('{"status":"success", "msg":"点赞"}', content_type='application/json')
        else:
            user_fav = UserFavoriteDirector()
            if int(fav_id) :
                director = Director.objects.get(id=int(fav_id))
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.director=director
                user_fav.save()
                director.fav_nums += 1
                director.save()
                return HttpResponse('{"status":"success", "msg":"已点赞"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"点赞出错"}', content_type='application/json')