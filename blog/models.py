from django.db import models
from django.contrib.auth.models import User


#blog应用的题目
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    #添加构造方法使返回的对象更易读
    def __str__(self):
        return self.type_name


#blog应用的内容
class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #添加构造方法使返回的对象更易读
    def __str__(self):
        return self.title

