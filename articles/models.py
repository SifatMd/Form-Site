from django.db import models
from django.contrib.auth.models import User
 

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True) #this
			#will automatically populate this field with time now
	
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


	def __str__(self):
		return self.title



	def snippet(self):
		string = self.body[:50] 
		if(len(string) == 50):
			string = string + " ..."

		return string
















