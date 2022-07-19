from django.db import models
from django.contrib.auth.models import User

#https://noauto-nolife.com/post/django-foreignkey-user/

class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    user        = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE, null=True,blank=True)


