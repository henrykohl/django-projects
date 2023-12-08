from django import forms

from .models import Product

# 23
# class ProductForm(forms.ModelForm):
# 	class Meta:
# 		model = Product
# 		fields = [
# 			'title',
# 			'description',
# 			'price'
# 		]

# 25 (label='...' 可以省略)
# class RawProductForm(forms.Form):
# 	title       = forms.CharField() # default: required=False
# 	description = forms.CharField(label='description')
# 	price       = forms.DecimalField(label='price')

# 26
class RawProductForm(forms.Form):  
	title       = forms.CharField(label='',
								widget=forms.TextInput(attrs={"placeholder": "Your title"})
								 )                      # label='' 頁面不顯示"title"
	description = forms.CharField(required=False, 
								widget=forms.Textarea(
									attrs = {
											"placeholder": "Your description",
											"class": "new-class-name two",
											"id": "my-id-for-textarea",
											"rows": 20,
											"cols": 120
											}
									)
								 )
	price       = forms.DecimalField(initial=199.99)    # default值=199.99
	# email       = forms.EmailField() # 自己加的

# 27
class ProductForm(forms.ModelForm):
	title       = forms.CharField(label='',
								widget=forms.TextInput(attrs={"placeholder": "Your title"})
								 )
	
	description = forms.CharField(required=False, 
								widget=forms.Textarea(
									attrs = {
											"placeholder": "Your description",
											"class": "new-class-name two",
											"id": "my-id-for-textarea",
											"rows": 20,
											"cols": 120
											}
									)
								 )
	price       = forms.DecimalField(initial=199.99)
	email       = forms.EmailField()

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
		]

	"""def clean_<my_field_name> (版本1)"""
	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title") 
	# 	print("CFE" in title)
	# 	if "CFE" in title:
	# 		return title
	# 	else:
	# 		raise forms.ValidationError("This is not a valid title")

	"""(版本2)"""
	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if not "CFE" in title:
	# 		raise forms.ValidationError("This is not a valid title")
	# 	if not "news" in title:
	# 		raise forms.ValidationError("This is not a valid title!")
	# 	return title

	# def clean_email(self, *args, **kwargs):
	# 	email = self.cleaned_data.get("email")
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("This is not a valid email")
	# 	return email

