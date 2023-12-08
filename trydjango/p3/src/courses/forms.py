from django import forms # default

from .models import Course # 43

class CourseModelForm(forms.ModelForm): # 43
	class Meta:
		model = Course
		fields = [
			'title'
		]
	
	# def clean_<fieldname>
	def clean_title(self): # 44
		title = self.cleaned_data.get('title')
		if title.lower() == 'abc':
			raise forms.ValidationError("This is not a valid title")
		return title
