from django.shortcuts import render # default

from django.http import HttpResponse

# Create your views here.
"""MVT - Model, View, Template"""
"""MVC - Model, View, Controller"""

def Welcome(request):
  # return HttpResponse('<h1>Hello World!</h1>')
  return render(request, 'index.html')

def User(request):
  username = request.GET['username']
  print(username)
  return render(request, 'user.html', {'name': username})