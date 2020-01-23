from django.shortcuts import get_object_or_404, render
from .models import Blog, BlogType


#主页视图
def index(request):
    blogs = Blog.objects.all()
    blog_types = BlogType.objects.all()
    context = {'blogs': blogs, 'blog_types': blog_types}
    return render(request, 'blog/index.html', context)


#博客页面视图
def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    blog_types = BlogType.objects.all()
    context = {'blog': blog, 'blog_types':blog_types}
    return render(request, 'blog/blog_detail.html', context)


#各分类博客视图
def blog_classification(request, blog_type_pk):
    blog_types = BlogType.objects.all()
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs = Blog.objects.filter(blog_type=blog_type)
    context = {'blog_types': blog_types, 'blog_type': blog_type, 'blogs': blogs}
    return render(request, 'blog/blog_classification.html', context)


def new_blog(request):
    blog_types = BlogType.objects.all()
    context = {'blog_types': blog_types}
    return render(request, 'blog/new_blog.html', context)