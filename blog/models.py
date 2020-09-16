from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
 

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'عنوان')
    article = models.TextField(verbose_name = 'متن')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'نویسنده')  
    pub_date = models.DateTimeField(default=timezone.now, verbose_name = 'تاریخ') 
    tags = TaggableManager()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author =  models.CharField(max_length=200,blank =True)
    massage = models.TextField()
    def __str__(self):
        return self.massage

