from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import article_list, article_detail, article_create


app_name = 'articles'

urlpatterns = [  
	url(r'^$', article_list, name="list"), 
	url(r'^create/$', article_create, name="create"),
	url(r'^(?P<slug>[\w-]+)/$', article_detail, name="detail"),
]






















