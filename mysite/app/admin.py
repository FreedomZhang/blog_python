#coding:utf-8
from django.contrib import admin
from .models import Tclass,Title,Tstate,Article,Label

admin.site.register(Tstate)
admin.site.register(Article)
admin.site.register(Tclass)
admin.site.register(Label)
