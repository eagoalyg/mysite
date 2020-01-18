from django.shortcuts import get_object_or_404, render
from .models import Blog, BlogType


def index(request):
    blogs = Blog.objects.all()
    blog_types = BlogType.objects.all()
    context = {'blogs': blogs, 'blog_types': blog_types}
    return render(request, 'blog/index.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)


def blog_classification(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs = Blog.objects.filter(blog_type=blog_type)
    context = {'blog_type': blog_type, 'blogs': blogs}
    return render(request, 'blog/blog_classification.html', context)

