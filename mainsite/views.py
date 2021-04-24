from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from .models import Post,Write
from .form import RegisterForm,LoginForm,WriteArticleForm

def plan(request):
    return render(request,"plan.html")

def article(request):
    posts = Write.objects.all()
    now = datetime.now()
    return render(request,"index.html",locals())

def showpost(request,id):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)

    try:
        post = Write.objects.get(id=id)
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

@login_required(login_url='/accounts/login')
def write_article(request):
    if request.user.is_authenticated:
        username = request.user.username

    write_form = WriteArticleForm()

    if request.method == "POST":
        user = User.objects.get(username=username)
        write_article = Write(user=user)
        write_form = WriteArticleForm(request.POST,instance=write_article)
        if write_form.is_valid():
            write_form.save()
            return redirect('/')
    return render(request,'write_article.html',locals())

@login_required(login_url='/accounts/login')
def update_article(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id

    try:
        article = Write.objects.get(id=id)
        if user_id != article.user.id:
            return redirect('/')
    except:
        return redirect('/')

    if request.method == "POST":
        write_form = WriteArticleForm(request.POST,instance=article)
        if write_form.is_valid():
            write_form.save()
            return redirect('/')
    return render(request,"update_article.html",locals())

@login_required(login_url='/accounts/login')
def delete_article(request,id):
    if request.method == "POST":
        post = Write.objects.get(id=id)
        post.delete()
        return redirect('/')

    try:
        post = Write.objects.get(id=id)

        if request.user.is_authenticated:
            user_id = request.user.id
        if user_id != post.user.id:
            return redirect('/')

        if post != None:
            return render(request,'delete_article.html',locals())
    except:
        return redirect('/article/' + str(id))



# Create your views here.
