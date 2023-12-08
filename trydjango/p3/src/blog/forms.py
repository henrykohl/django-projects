from django import forms # 38

from .models import Article # 38

class ArticleModelForm(forms.ModelForm): # 38
	class Meta: 
		model = Article
		fields = (
			'title',
			'content',
			'active',
		)