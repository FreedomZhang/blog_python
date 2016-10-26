#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
标题表(tb_Title)
ID	标题名称	备注	预留URL	预留字段1	预留字段2
TitleID	TitleName	Remarks	ResUrl	Reserve1	Reserve2

'''
#标题
class Title(models.Model):
    titleID=models.CharField('ID',default='',max_length=50)
    titleName=models.CharField('标题名称',max_length=50)
    remarks=models.TextField('备注',max_length=500)
    resUrl=models.CharField('预留URL',max_length=100)
    reserve1 = models.CharField('预留字段1', max_length=100)
    reserve2 = models.CharField('预留字段2', max_length=100)
    def __str__(self):
        return  self.titleName

'''
分类(tb_Class)
ID	分类名称	备注	父级分类编号	预留字段1	预留字段2
ClassID	ClassName	Remarks	ParentID	Reserve1	Reserve2

'''
#分类
class Tclass(models.Model):
    classID=models.CharField('ID',default='',max_length=50,blank=True)
    className=models.CharField('分类名称',max_length=50)
    remarks=models.TextField('备注',max_length=500,blank=True)
    parentID=models.CharField('父级ID',max_length=50,blank=True)
    reserve1 = models.CharField('预留字段1', max_length=100,blank=True)
    reserve2 = models.CharField('预留字段2', max_length=100,blank=True)
    def __str__(self):
        return  self.className

'''
标签(tb_Label)
ID	标签	备注	预留字段1	预留字段2
LabelID	LabelName	Remarks	Reserve1	Reserve2
'''
#标签
class Label(models.Model):
    labelID=models.CharField('ID',default='',max_length=50,blank=True)
    labelName=models.CharField('标签名称',max_length=50)
    remarks = models.TextField('备注', max_length=500,blank=True)
    reserve1 = models.CharField('预留字段1', max_length=100,blank=True)
    reserve2 = models.CharField('预留字段2', max_length=100,blank=True)
    def __str__(self):
        return  self.labelName

'''
状态表(tb_State)
ID	状态名称	备注	预留字段1	预留字段2
StateID	StateName	Remarks	Reserve1	Reserve2
'''
#状态
class Tstate(models.Model):
    statID=models.CharField('ID',default='',max_length=50)
    stateName=models.CharField('状态名称',max_length=50)
    remarks = models.TextField('备注', max_length=500,null=True,blank=True)
    reserve1 = models.CharField('预留字段1', max_length=100,null=True,blank=True)
    reserve2 = models.CharField('预留字段2', max_length=100,null=True,blank=True)
    def __str__(self):
        return  self.stateName

'''
文章(tb_Article)
ID	分类	标题	内容	发布时间	作者	阅读量	状态	标签	附件	预留字段1	预留字段2
ArticleID	ClassName	Titele	Article	ReleaseTime	Author	ClickVolume	State	Labels	Enclosures	Reserve1	Reserve2
'''
#文章
class Article(models.Model):
    articleID=models.CharField('ID',default='',max_length=50,blank=True)
    className=models.CharField('分类',max_length=50)
    titele=models.CharField('标题',max_length=50)
    article=models.TextField('内容',max_length=5000)
    releaseTime=models.DateTimeField('创建时间',default=timezone.now)
    author=models.CharField('作者',max_length=50,blank=True)
    clickVolume=models.CharField('点击量',max_length=50,blank=True)
    tstate=models.CharField('状态',max_length=50,blank=True)
    labels=models.CharField('标签',max_length=50,blank=True)
    enclosures=models.CharField('附件地址',max_length=50,blank=True)
    reserve1 = models.CharField('预留字段1', max_length=100,blank=True)
    reserve2 = models.CharField('预留字段2', max_length=100,blank=True)
    def __str__(self):
        return  self.titele

'''
评论(tb_Comment)
ID	文章id	评论内容	评论时间	评论人	预留字段1	预留字段2
CommentID	ArticleID	Content	CommentTime	CommentPel	Reserve1	Reserve2
'''
#评论
class Comment(models.Model):
    commentID=models.CharField('ID',default='',max_length=50)
    articleID=models.CharField('文章id',max_length=50)
    content=models.CharField('评论内容',max_length=50)
    commentTime=models.DateTimeField('评论时间',default=timezone.now())
    commentPel=models.CharField('评论人',max_length=50)
    reserve1 = models.CharField('预留字段1', max_length=100)
    reserve2 = models.CharField('预留字段2', max_length=100)
    def __str__(self):
        return  self.content

'''
附件表(tb_Enclosure)
ID	文件类型	文件原名称	文件唯一名称	文件路径	上传时间	预留字段1	预留字段2
EnclosureID	EnclosureType	LName	WName	ERoute	ETime	Reserve1	Reserve2
'''
#附件
class Enclosure(models.Model):
    enclosureID=models.CharField('ID',default='',max_length=50)
    enclosureType=models.CharField('文件类型',max_length=50)
    lname=models.CharField('原名称',max_length=50)
    wname=models.CharField('文件唯一名称',max_length=50)
    eroute=models.CharField('文件路径',max_length=50)
    etime=models.DateTimeField(default=timezone.now())
    reserve1 = models.CharField('预留字段1', max_length=100)
    reserve2 = models.CharField('预留字段2', max_length=100)
    def __str__(self):
        return  self.lname
