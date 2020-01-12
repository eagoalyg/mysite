from django.contrib import admin
from .models import Title, Content


#注册Title
admin.site.register(Title)


#注册Content
admin.site.register(Content)
