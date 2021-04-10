from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
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
def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login2')

    context = {
        'form':form
    }
    return render(request,'login.html',context)
def test(request):
    return render(request,'test.html')


# Create your views here.
