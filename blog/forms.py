from .models import Blog
from django.forms import ModelForm


class Blog(models.Model):
	class Meta:
		model = Blog
		fields = ['blog_type', 'title', 'author', 'content']