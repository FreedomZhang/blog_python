from django.shortcuts import render
from .models import Article
def index(request):
    article=Article.objects.all()
    return  render(request,'app/index.html',{'article':article})
