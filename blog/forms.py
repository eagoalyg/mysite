from .models import Blog
from django.forms import ModelForm


class NewBlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'blog_type', 'content']