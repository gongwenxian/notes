from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
	return render_to_response('search.html')

def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		message='你搜索的内容为：'+request.GET['q']
	else:
		message='您提交了空表单！'
	return HttpResponse(message)
