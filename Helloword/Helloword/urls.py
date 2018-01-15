from django.conf.urls import url
from django.contrib import admin
from . import view,search,searchpost

urlpatterns=[
	url(r'^admin/',admin.site.urls),
	url(r'^hello$',view.abd),
	url(r'^search$',search.search),
	url(r'^search-form$',search.search_form),
	url(r'^search-post$',searchpost.search_post),
]
