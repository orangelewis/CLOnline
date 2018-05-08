"""PycharmProjectsCLOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.static import serve
from django.views.generic import TemplateView
import xadmin


from users.views import LoginView,RegisterView,AciveUserView,ForgetPwdView,ResetView,ModifyPwdView,LogoutView,IndexView
from PycharmProjectsCLOnline.settings import MEDIA_ROOT#,STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),

    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),

    url('^register/$',RegisterView.as_view(),name="register"),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),





    #地区
    url(r'^region/', include('region.urls',namespace="reg")),
    #电影
    url(r'^film/', include('film.urls',namespace="film")),
    #用户
    url(r'^users/', include('users.urls',namespace="users")),
    #文章
    url(r'^article/', include('article.urls',namespace="article")),

    url(r'^ueditor/',include('DjangoUeditor.urls' )),

]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'