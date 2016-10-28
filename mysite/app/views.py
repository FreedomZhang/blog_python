#coding:utf-8
from django.shortcuts import render,get_object_or_404
from .models import Article,Tclass,Label
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
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
def addArticle(request):
    if request.method=='GET':
        return render(request,'',{})
    if request.method=='POST':
        titele =request.POST['titele']
        article =request.POST['article']
        className =request.POST['className']
        labels =request.POST['labels']
        releaseTime=timezone.now()
        obj=Article(titele=titele,article=article,className=className,labels=labels,releaseTime=releaseTime)
        obj.save()
        return redirect(reverse('articlelist'))


@login_required
def addview(request):
    tclass=Tclass.objects.all()
    tlable=Label.objects.all()
    return  render(request,'app/addArticle.html',{'tclass':tclass,'tlable':tlable})

@login_required
def admin_base(request):
    return  render(request,'app/admin_base.html',{})


@login_required
def log_out(request):
    logout(request)

#@login_required
def aedit(request):
    pass

@csrf_exempt
def article_remove(request):
    if request.method == 'GET':
        return render(request, '', {})
    if request.method == 'POST':
        Rid=request.POST['id']
        article=get_object_or_404(Article,id=Rid)
        article.delete()
        return  HttpResponse('OK')


def articlelist(request):
    article=Article.objects.all()
    return  render(request,'app/articlelist.html',{'article':article})

