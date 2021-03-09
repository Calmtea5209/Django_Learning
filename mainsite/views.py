from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
def homepage(request):
    return render(request,"main.html")
def article(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,"article.html",locals())
# Create your views here.
