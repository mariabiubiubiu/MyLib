from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#http://maplye.iteye.com/blog/448960
#直接使用django的用户模块

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)


    def __str__(self):  # 在python2版本中使用的是__unique__
        return self.user.username







class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateField()
    category = models.CharField(max_length=128)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name

