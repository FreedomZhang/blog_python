#coding:utf-8
from django.conf.urls import url,include,handler400,handler403,handler404,handler500
from django.contrib import admin
from app import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$',include('app.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/',views.login_index,name='login'),
    url(r'^admint/',views.log_in,name='log_in'),
    url(r'^admin_base/',views.admin_base,name='admin_base'),
    url(r'^add/',views.addview,name='add'),
    url(r'^addArticle/',views.addArticle,name='addArticle'),
    url(r'^articlelist',views.articlelist,name='articlelist'),
    url(r'^article_remove',views.article_remove,name='article_remove'),
    url(r'^page',views.GetPageList,name='GetPageList'),
    #url(r'^api/', views.GetT, name='GetT'),
]
handler404="app.views.page_not_found404"