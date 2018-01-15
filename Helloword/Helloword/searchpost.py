from django.shortcuts import render
from django.views.decorators import csrf

def search_post(request):
	c={}
	if request.POST:
		c['rlf']=request.POST['q']
	return render(request,'post.html',c) 
