from django.urls import path
from .views import (
	ArticleCreateView,  # 38
    ArticleDeleteView,  # 39
    ArticleDetailView,  # 37
    ArticleListView,    # 36
    ArticleUpdateView   # 38
)

app_name = 'articles' # 36
urlpatterns = [
    path('',ArticleListView.as_view(), name='article-list'),                     # 36
    path('create/', ArticleCreateView.as_view(), name='article-create'),         # 38
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),       # 37 
    path('<int:pk>/update/',ArticleUpdateView.as_view(), name='article-update'), # 38
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article-delete'), # 39
]