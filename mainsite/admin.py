from django.contrib import admin
from .models import Post,Write
class PostAdmin(admin.ModelAdmin):
    list_display=("title","slug","pub_date")

admin.site.register(Post,PostAdmin) #register model
admin.site.register(Write)
# Register your models here.
