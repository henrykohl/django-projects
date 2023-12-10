# This file is created manually
from django.urls import path
from . import views

urlpatterns = [
  # path('', views.Welcome),
  # path('django', views.Welcome)
  path('', views.Welcome, name='Welcome'),
  path('user', views.User, name='User')
]