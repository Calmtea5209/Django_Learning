from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Write,Profile

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    nickname = forms.CharField(
        label="暱稱",
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model=User
        fields = ('username', 'nickname', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
class WriteArticleForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ['title','context']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','gender']

