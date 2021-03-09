from django.db import models
from django.utils import timezone

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
