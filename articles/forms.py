#all model forms for articles will be in this file

from django import forms
from . import models




class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'body', 'slug', 'thumb']
		






























