from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-pub_date',) #文章顯示依時間依序顯示
    def __str__(self):
        return self.title
# Create your models here.

class Write(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(u"標題",default="",max_length=200)
    context = RichTextField(u"內容",default="")
    pub_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title