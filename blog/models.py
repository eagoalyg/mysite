from django.conf import settings
from django.db import models


#blog应用的题目
class Title(models.Model):
    title = models.CharField(max_length=30)
    #添加构造方法使返回的对象更易读
    def __str__(self):
        return self.title


#blog应用的内容
class Content(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    contetnt = models.CharField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #添加构造方法使返回的对象更易读
    def __str__(self):
        return self.title

