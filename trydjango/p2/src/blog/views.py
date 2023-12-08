from django.shortcuts import render, get_object_or_404
from django.urls import reverse # 為delete專用

# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	ListView,
	DeleteView
	)

from .models import Article
from .forms import ArticleModelForm

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	"""方法一&二：在create頁面按下save後,會導到首頁如果改成/blog,就會導到 首頁/blog/"""
	success_url = '/blog'      # 方法一

	"""測試用"""
	# def form_valid(self, form):
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

	# def get_success_url(self): # 方法二
	# 	return '/blog'

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all() # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	queryset = Article.objects.all()

	# queryset = Article.objects.filter(id__gt=1)

	"""This is built-in to class based views, especially with detail views,"""
	def get_object(self):
		# print(self.kwargs)
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	# success_url = '/'

	def get_object(self):
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Article, id=id_)

	# def form_valid(self, form):
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

	# def get_success_url(self):
	# 	return '/'

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'
	# queryset = Article.objects.all()     # 對ImproperlyConfigured 的No URL to redirect to. 的錯誤,沒有用
	"""法一"""
	# success_url = '/blog/'               
	

	def get_object(self):
		id_ = self.kwargs.get("pk")
		return get_object_or_404(Article, id=id_)

	"""法二"""
	def get_success_url(self):
		# return reverse('blog:list-view')         # 沒特殊用途
		# print(reverse('articles:article-list'))  # 測試用
		return reverse('articles:article-list')
	
	"""法三"""
	# s_l = '/blog/'
	# def get_success_url(self):
	# 	return self.s_l