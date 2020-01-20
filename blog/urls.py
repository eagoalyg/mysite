'''
    blog软件的url路径
'''
from django.urls import path

from . import views

app_name = 'blog'
#主页的url
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:blog_type_pk>/', views.blog_classification, name='blog_classification'),
]
