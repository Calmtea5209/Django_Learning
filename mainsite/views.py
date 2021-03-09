from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post
def homepage(request):
    return render(request,"main.html")
def article(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,"article.html",locals())
def showpost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request,'showpost.html',locals())
    except:
        return redirect('/')


# Create your views here.
