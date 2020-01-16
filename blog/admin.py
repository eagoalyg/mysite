from django.contrib import admin
from .models import BlogType, Blog


#注册BlogType
admin.site.register(BlogType)


#注册Blog
admin.site.register(Blog)
