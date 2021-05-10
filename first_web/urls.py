"""first_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainsite.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/<int:id>/',showpost,name="article-url"),
    path('article/delete/<int:id>/',delete_article,name="article-delete"),
    path('article/update/<int:id>/',update_article,name="article-update"),
    path('article/write/',write_article,name="article-write"),
    path('accounts/register/',register,name="accounts-register"),
    path('accounts/login/',signin,name="accounts-login"),
    path('accounts/logout/',signout,name="accounts-logout"),
    path('profile/<int:id>',showprofile,name="profile-url"),
    path('plan/',plan),
    path('',article),
    
]
