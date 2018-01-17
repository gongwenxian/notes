from django.shortcuts import render

def print(request):
	a={}
	a['name']="charming prince!"
	return render(request,"v.html",a)
