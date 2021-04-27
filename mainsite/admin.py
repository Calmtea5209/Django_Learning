from django.contrib import admin
from .models import Post,Write,Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
class PostAdmin(admin.ModelAdmin):
    list_display=("title","slug","pub_date")

admin.site.register(Post,PostAdmin) #register model
admin.site.register(Write)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','nickname')

class ProfileInline(admin.StackedInline): #把Profile加進User model
    model=Profile
    can_delete = False

class UserAdmin(BaseUserAdmin): #定義Admin
    inlines = (ProfileInline,)
    list_display = ('username','nickname','email','is_staff','is_active','is_superuser')
    def nickname(self,obj):
        return obj.profile.nickname
    nickname.short_description = "暱稱"

admin.site.unregister(User) #重新註冊Admin
admin.site.register(User,UserAdmin)
# Register your models here.
