from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .form import RegisterForm,LoginForm

def plan(request):
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
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')

    return render(request,'register.html',locals())
def signin(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'signin.html',locals())
def signout(request):
    logout(request)
    return redirect('/')

def test(request):
    return render(request,'test.html')


# Create your views here.
