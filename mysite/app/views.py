from django.shortcuts import render
from .models import Article,Tclass
def index(request):
    article=Article.objects.all()
    tclass=Tclass.objects.all()

    return  render(request,'app/index.html',{'article':article,'tclass':tclass})
