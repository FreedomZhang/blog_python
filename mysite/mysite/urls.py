"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
]
