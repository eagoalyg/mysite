from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)


def program(request):
    response = "You are looking at program"
    return HttpResponse(response)


def diary(request):
    response = "You are looking at diary"
    return HttpResponse(response)
