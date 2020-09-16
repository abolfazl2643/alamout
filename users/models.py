from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='image')
    img = models.ImageField(upload_to = 'images',blank = True)
    username = models.CharField(max_length=200 , default = '',blank = True)
    def __str__(self):
        return 'username : {}  '.format(self.user)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)