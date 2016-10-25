#coding:utf-8
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.index),#首页路由
    #url(r'^post/(?P<pk>[0-9]+)/$',views.detailt,name='detailt'),
]