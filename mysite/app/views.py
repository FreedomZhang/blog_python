#coding:utf-8
import  re
from django.shortcuts import render,get_object_or_404
from .models import Article,Tclass,Label
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
#from rest_framework import request,permissions
#from rest_framework.response import Response
#from rest_framework.decorators import api_view, permission_classes
from django.core import serializers
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.conf.urls import handler400,handler403,handler404,handler500


def index(request):
    article=Article.objects.all()[:4]
    tclass=Tclass.objects.all()
    tlables=Label.objects.all()
    return  render(request,'app/index.html',{'article':article,'tclass':tclass,'tlables':tlables})

def detail(request,question_id):
    article=Article.objects.get(id=question_id)
    cliknum=article.clickVolume
    article.clickVolume=int(cliknum)+1
    article.save()
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
            return render(request, 'app/admin_base.html', {"username":username})
        else:
            return render(request,'app/signin.html',{})

#更改不同标签的统计数目
def Reserve1Num(className,labels,type):
    if type>0:
        objt = Tclass.objects.get(className=className)
        objt.reserve1 = int(objt.reserve1) + 1
        objt.save()
        if len(labels)>1:
            labelsArr = re.split(',', labels)
            for item in labelsArr:
                objl = Label.objects.get(labelName=item)
                objl.reserve1 = int(objl.reserve1) + 1
                objl.save()
    if type<0:
        objt = Tclass.objects.get(className=className)
        objt.reserve1 = int(objt.reserve1) - 1
        objt.save()
        if len(labels)>1:
            labelsArr = re.split(',', labels)
            for item in labelsArr:
                objl = Label.objects.get(labelName=item)
                objl.reserve1 = int(objl.reserve1) - 1
                objl.save()

@login_required
def addArticle(request):
    if request.method=='GET':
        return render(request,'',{})
    if request.method=='POST':
        titele =request.POST['titele']
        article =request.POST['article']
        className =request.POST['className']
        labels =request.POST['labels']
        clickVolume='0'
        releaseTime=timezone.now()
        obj=Article(titele=titele,article=article,className=className,labels=labels,releaseTime=releaseTime,clickVolume=clickVolume)
        obj.save()
        Reserve1Num(className,labels,1)
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

@login_required
@csrf_exempt
def article_remove(request):
    if request.method == 'GET':
        return redirect(reverse('articlelist'))
    if request.method == 'POST':
        Rid=request.POST['id']
        article=get_object_or_404(Article,id=Rid)
        article.delete()
        #return redirect(reverse('articlelist'))
        Reserve1Num(article.className, article.labels, -1)
        return  HttpResponse('OK',content_type='application/javascript')

@login_required
def articlelist(request):
    article=Article.objects.all()
    return  render(request,'app/articlelist.html',{'article':article})

#分页
@csrf_exempt
def GetPageList(request):
    if request.method == 'POST':
        #page = request.POST['page']
        arcount=int(request.POST['arcount'])
        artic=Article.objects.all()[arcount:arcount+4]
        json_data = serializers.serialize("json", artic)
        return HttpResponse(json_data,content_type='application/javascript')
'''
@api_view(['GET','PUT','DELETE','POST'])
@permission_classes((permissions.AllowAny,))
def GetT(request):
    if request.method=='POST':
        titele = request.POST['titele']
        article = request.POST['article']
        className = request.POST['className']
        labels = request.POST['labels']
        releaseTime = timezone.now()
        obj = Article(titele=titele, article=article, className=className, labels=labels, releaseTime=releaseTime)
        obj.save()
        json_data = serializers.serialize("json", Article.objects.all())
        response = HttpResponse(json_data)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    if request.method=='GET':
        json_data = serializers.serialize("json", Article.objects.all())
        response = HttpResponse(json_data)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
'''
#404页码
def page_not_found404(request):
    return render(request,'404.html',{})


