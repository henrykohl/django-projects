from django.shortcuts import render, get_object_or_404
from django.urls import reverse # 為delete專用

# Create your views here.
from django.views.generic import (
	CreateView, # 38
	DetailView, # 37
	ListView,   # 36
	UpdateView, # 38
	DeleteView  # 39
	)

from .models import Article # 36
from .forms import ArticleModelForm # 38

class ArticleCreateView(CreateView): # 38 
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()

	"""方法1&2: 在create頁面按下save後,會導到首頁如果改成/blog,就會導到 首頁/blog/"""
	# success_url = '/blog'      # 方法1
	"""測試用"""
	# def form_valid(self, form):
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

	def get_success_url(self): # 方法2
		return '/blog'

class ArticleListView(ListView): # 36
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all() # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView): # 37
	template_name = 'articles/article_detail.html'
	"""方法1"""
	# queryset = Article.objects.all() 
	"""方法-測試用"""
	# queryset = Article.objects.filter(id__gt=1) 

	"""方法2:This is built-in to class based views, especially with detail views,"""
	def get_object(self):
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView): # 38
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	"""方法1&2"""
	# success_url = '/blog' # 方法1
	
	def get_object(self):
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Article, id=id_)
	"""測試用"""
	# def form_valid(self, form):
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

	def get_success_url(self): # 方法2
		return '/blog'

class ArticleDeleteView(DeleteView): # 39
	template_name = 'articles/article_delete.html'
	# queryset = Article.objects.all()     # 對ImproperlyConfigured 的No URL to redirect to. 的錯誤,沒有用             
	

	def get_object(self):
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Article, id=id_)

	"""法一"""
	# success_url = '/blog/'

	"""法二"""
	def get_success_url(self):
		# return reverse('blog:list-view')         # 沒特殊用途
		# print(reverse('articles:article-list'))  # 測試用
		return reverse('articles:article-list')
	
	"""法三"""
	# s_l = '/blog/'
	# def get_success_url(self):
	# 	return self.s_l