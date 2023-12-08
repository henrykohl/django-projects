from django.urls import path
from .views import (
	ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView
)

app_name = 'articles'
urlpatterns = [
    path('',ArticleListView.as_view(), name='article-list'),                  # 36
    path('create/', ArticleCreateView.as_view(), name='article-create'),              # 35
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),          # 37 
    path('<int:pk>/update/',ArticleUpdateView.as_view(), name='article-update'), # 35
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article-delete'), # 31
]