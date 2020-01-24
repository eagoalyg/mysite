from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from .forms import NewBlogForm
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
    user = User.objects.first()
    if request.method == 'POST':
        form = NewBlogForm(request.POST)
        if form.is_valid():
            # TODO: 重写以下代码    
            # blog = form.save()
            # blog.title = title
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # blog_type = form.cleaned_data['blog_type']
            # created_at = form.cleaned_data['created_at']
            # user = user
            # return redirect('blog:index')
            pass
    else:
        form = NewBlogForm()
        context = {'form': form, 'blog_types': blog_types}
    return render(request, 'blog/new_blog.html', context)