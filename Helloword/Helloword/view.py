#from django.http import HttpResponse
from django.shortcuts import render

def abd(request):
	#return HttpResponse("Hello!Gwx!")
	content={}
	content['hello']="Charming Prince~"
	return render(request,'hello.html',content)
