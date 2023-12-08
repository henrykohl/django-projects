"""
URL configuration for studybud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # default
from django.urls import path, include # path 為 default, include 為 新增

# from django.http import HttpResponse # 

# def home(request):   #
#     return HttpResponse('Home page')

# def room(request):   # 
#     return HttpResponse('ROOM')

from django.shortcuts import render

def adm(request):
    return render(request, 'admain.html') 

def tem(request):
    return render(request, 'tem.html') 

def test(request):
    return render(request, 'test3.html')

urlpatterns = [
    path('admin/', admin.site.urls), # default
    # path('', home),        # 
    # path('room/', room),   # 
    path('', include('base.urls')),  # 新增

    path('adm/', adm), 
    path('tem/', tem),
    
    path('test/', test),
] 
