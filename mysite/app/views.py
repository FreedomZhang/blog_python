#coding:utf-8
from django.shortcuts import render,get_object_or_404
from .models import Article,Tclass
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect


def index(request):
    article=Article.objects.all()
    tclass=Tclass.objects.all()

    return  render(request,'app/index.html',{'article':article,'tclass':tclass})

def detail(request,question_id):
    article=Article.objects.get(id=question_id)
    return render(request,'app/detail.html',{'article':article})

def login_index(request):
    return  render(request,'app/signin.html',{})

def log_in(request):
    if  request.method=='GET':
        return render(request, 'app/signin.html', {})
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)#创建登陆记录
            #return render(request, 'app/admin_base.html', {})
            return HttpResponseRedirect('/admin_base/')#重定向到管理员首页

        else:
            return render(request,'app/signin.html',{})
@login_required
def admin_base(request):
    return  render(request,'app/admin_base.html',{})


@login_required
def log_out(request):
    logout(request)

#@login_required
def aedit(request):
    pass