from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import CreateArticle
#decorator
from django.contrib.auth.decorators import login_required


def article_list(request):
	articles = Article.objects.all().order_by("date")

	return render(request, 'articles/article_list.html', {'articles' : articles})




def article_detail(request, slug):
	article = Article.objects.get(slug=slug)

	return render(request, 'articles/article_detail.html', {'article':article})



#this decorator is protecting the article_create view function
#so if user is logged in, then only this function will fire
@login_required(login_url="/accounts/login/")
def article_create(request):

	if request.method == 'POST':
		form = CreateArticle(request.POST, request.FILES)
		#request.FILES is done coz we are uploading an image i.e. file, so a separate
		#request.FILES must be done

		if form.is_valid():
			#save this article to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			
			return redirect("articles:list")

	else:
		form = CreateArticle()

	return render(request, "articles/article_create.html", {'form':form})















