from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
# def home_view(*args, **kwargs): # *args, **kwargs
# 	return HttpResponse("<h1>Hello World</h1>") # string of HTML code

# def home_view(*args, **kwargs): # *args, **kwargs
def home_view(request, *args, **kwargs):
	# print(args, kwargs)
	# print(request)
	# print(request.user)
	# return HttpResponse("<h1>Hello World</h1>") 
	return render(request,"home.html",{}) 

def contact_view(request, *args, **kwargs): # *args, **kwargs
	# return HttpResponse("<h1>Contact Page</h1>")
	return render(request,"contact.html",{})

def about_view(request, *args, **kwargs): # *args, **kwargs
	# return HttpResponse("<h1>About Page</h1>")
	# return render(request,"about.html",{})

	my_context = {
		"my_text": "abc This is about us",     # 17
		"this_is_true": True,                  # 19
		"my_number": 123,                      # 17
		"my_list": [1313, 4231, 312, "Abc"],   # 17
		"my_html": "<h1>Hello World</h1>",     # 20
	}

	# 壞方法
	# for item in [123,456,789]:
	# 	my_context['item1']=item
	return render(request,"about.html", my_context)

def social_view(request, *args, **kwargs): # *args, **kwargs
	return HttpResponse("<h1>Social Page</h1>")