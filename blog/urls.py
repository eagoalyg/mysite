'''
    blog软件的url路径
'''
from django.urls import path

from . import views


#主页的url
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_pk', views.blog_detail, name='blog_detail'),
    path('diary', views.diary, name='diary'),
]
