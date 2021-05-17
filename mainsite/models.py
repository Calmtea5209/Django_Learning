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
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    GENDER = (('男性', '男性'),('女性', '女性'),('其他', '其他'),('不公開', '不公開'))
    gender = models.CharField(u'性別',choices=GENDER,max_length=10,default='不公開')
    nickname = models.CharField(u"暱稱",max_length=20,default="無")
    image = models.ImageField(u'照片',upload_to='%Y/%m/%d/',default='default.png')
    intro = models.CharField(u"自我介紹",default="這個人很懶，什麼也沒打",max_length=100)
    def __str__(self):
        return self.user.username

class Write(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(u"標題",default="",max_length=200)
    context = RichTextField(u"內容",default="")
    pub_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title