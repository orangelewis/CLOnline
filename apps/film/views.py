from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Film ,FilmResource,Video,BanWord
from userOperation.models import UserFavoriteFilm,FilmComments,UserScore
from utils.mixin_utils import LoginRequiredMixin
from utils.get_score import get_score


# Create your views here.


class FilmListView(View):
    def get(self,request):
        all_films = Film.objects.all().order_by("-add_time")

        hot_films = Film.objects.all().order_by("-click_nums")[:3]



        # 电影搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_films = all_films.filter(
                Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) |
                Q(category__icontains=search_keywords))

        # 电影排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_films = all_films.order_by("-students")
            elif sort == "hot":
                all_films = all_films.order_by("-click_nums")

        # 对电影进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_films, 12, request=request)

        films = p.page(page)

        return render(request, 'film-list.html', {
            "all_films": films,
            "sort": sort,
            "hot_films": hot_films
        })


class VideoPlayView(LoginRequiredMixin,View):
    """
    视频播放页面
    """
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        film = video.film
        film.click_nums += 1
        film.save()
        #查询用户是否已经关联了该电影
        user_films = UserFavoriteFilm.objects.filter(user=request.user,film = film)
        if not user_films:
            user_film = UserFavoriteFilm(user=request.user,film=film)
            user_film.save()

        user_filmers = UserFavoriteFilm.objects.filter(film=film)
        user_ids = [user_filmer.user.id for user_filmer in user_filmers]
        all_user_films = UserFavoriteFilm.objects.filter(user_id__in=user_ids)


        film_ids = [user_filmer.film.id for user_filmer in all_user_films]


        relate_films = Film.objects.filter(id__in=film_ids).order_by("-click_nums")[:5]
        all_resources = FilmResource.objects.filter(film=film)

        film_id = video.film_id


        #评论
        all_comments = FilmComments.objects.filter(film_id=int(film_id)).order_by("-id")

       #收藏
        has_film_faved = False
        if request.user.is_authenticated():
            if UserFavoriteFilm.objects.filter(user=request.user, fav_id=film.id):
                has_film_faved = True

        #评分
        douban_id = film.doubanId
        webscore = get_score(douban_id)

        average = 0
        if request.user.is_authenticated():


            total = film.score
            s_nums = film.score_nums

            if s_nums != 0:
                average = total/s_nums

        #敏感词
        banWord = BanWord.objects.all().order_by("-add_time")


        return render(request, "film-play.html", {
            "film": film,
            "film_resources": all_resources,
            "relate_films": relate_films,
            "video": video,
            "all_comments": all_comments,
            "has_film_faved":has_film_faved,
            "douban_score": webscore["douban_score"],
            "imdb_score": webscore["imdb_score"],
            "average": average,
            "douban_id":douban_id,
            "banWord":banWord,


        })


class AddComentsView(View):
    """
    用户添加评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        film_id = request.POST.get("film_id", 0)
        comments = request.POST.get("comments", "")
        if int(film_id) > 0 and comments:
            film_comments = FilmComments()
            film = Film.objects.get(id=int(film_id))
            film_comments.film = film
            film_comments.comments = comments
            film_comments.user = request.user
            film_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


class DelCommentView(View):
    """
    用户删除评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        comment_id = request.POST.get("comment_id",0)
        exist_comment = FilmComments.objects.filter(id = comment_id)
        exist_comment.delete()
        return HttpResponse('{"status":"success", "msg":"删除成功"}', content_type='application/json')

class AddFavFilmView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)


        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavoriteFilm.objects.filter(user=request.user, film_id=int(fav_id))
        if exist_records:
            #如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            film = Film.objects.get(id=int(fav_id))
            film.fav_nums -= 1
            if film.fav_nums < 0:
                film.fav_nums = 0
            film.save()


            return HttpResponse('{"status":"success", "msg":"点赞"}', content_type='application/json')
        else:
            user_fav = UserFavoriteFilm()
            if int(fav_id) :
                film = Film.objects.get(id=int(fav_id))
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.film=film
                user_fav.save()
                film.fav_nums += 1
                film.save()



                return HttpResponse('{"status":"success", "msg":"已点赞"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"点赞出错"}', content_type='application/json')


class AddScoreView(View):
    """
    用户评分
    """

    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        film_id = request.POST.get("film_id", 0)
        film = Film.objects.get(id=int(film_id))
        user = request.user
        score = request.POST.get("score",0)


        userscore = UserScore()
        userscore.film = film
        userscore.user =user
        userscore.film_id =film_id
        userscore.score = score
        film.score += float(score)
        film.score_nums += 1


        exist_records = UserScore.objects.filter(film_id=int(film_id), user=user)
        if exist_records:
            film.score_nums -= 1
            exist_film = UserScore.objects.get(film_id=int(film_id), user=user)
            film.score -= exist_film.score
            exist_records.delete()
        userscore.save()
        film.save()

        return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')


