from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Film_article

# Create your views here.
class Film_articleView(View):
    def get(self,request):
        all_articles = Film_article.objects.all().order_by("-create_date")

        hot_articles = Film_article.objects.all().order_by("-click_nums")[:3]



        # 电影搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_articles = all_articles.filter(
                Q(title__icontains=search_keywords))

        # 电影排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_articles = all_articles.order_by("-students")
            elif sort == "hot":
                all_articles = all_articles.order_by("-click_nums")

        # 对电影进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 12, request=request)

        articles = p.page(page)

        return render(request, 'article-list.html', {
            "all_articles": articles,
            "sort": sort,
            "hot_articles": hot_articles
        })


class ArticleDetailView(View):
    def get(self, request, url_object_id):
        article = Film_article.objects.get(url_object_id=url_object_id)
        article.click_nums += 1
        article.save()


        sorted_article = Film_article.objects.all().order_by("-click_nums")[:3]
        return render(request, "article-detail.html", {
            "article": article,
            "sorted_article": sorted_article,

        })