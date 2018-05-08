# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/22 下午10:09'


from django.conf.urls import url, include

from .views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView,MyFilmView,MyFavDirectorView,MymessageView,LogoutView




urlpatterns = [
    #用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),

    # #用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    #
    # #用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    #
    # #发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    #
    # #修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    #
    # #我的课程
    url(r'^myfilm/$', MyFilmView.as_view(), name="myfilm"),
    #
    # #我收藏的课程机构
    # url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    #
    # #我收藏的授课讲师
    url(r'^mydirector/$', MyFavDirectorView.as_view(), name="myfav_director"),
    #
    # #我收藏的课程
    # url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    #
    # #我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),
]