'''
    blog软件的url路径
'''
from django.urls import path

from . import views


#主页的url
urlpatterns = [
    path('', views.index, name='index'),
    path('program', views.program, name='program'),
    path('diary', views.diary, name='diary'),
]
