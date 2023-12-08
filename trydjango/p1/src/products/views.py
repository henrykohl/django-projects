from django.shortcuts import render, get_object_or_404, redirect

from .models import Product # (當下目錄中的models中Product類) 節21/22

from .forms import ProductForm, RawProductForm 

from django.http import Http404

# Create your views here.


# 35 (開啟27或23, 31, 32, 附35)
def product_update_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)
# 附35
def product_detail_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)
	context = {
		"object": obj
	}
	return render(request, "products/product_detail.html", context)


# 21/22
# def product_detail_view(request):
# 	obj = Product.objects.get(id=1)
# 	"""基礎方式"""
# 	# context = {
# 	# 	'title': obj.title,
# 	# 	'description': obj.description
# 	# }
# 	"""通用方式"""
# 	context = {
# 		'object': obj
# 	}
# 	# 使用C:\Users\customer\dev\trydjango\src\templates\目錄下的product中detail.html
# 	# return render(request, "product/detail.html", context)   

#     # 使用C:\Users\customer\dev\trydjango\src\products\templates\products中product_detail.html
# 	return render(request, "products/product_detail.html", context)

"""23 - Django Model Forms"""
# def product_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()  # 此行讓資料新增後，頁面會被reset(rerender the form)

# 	context = {
# 		'form': form
# 	}
# 	# 使用C:\Users\customer\dev\trydjango\src\products\templates\products中product_create.html
# 	return render(request, "products/product_create.html", context)

# 24 - Raw HTML Forms
# def product_create_view(request):
# 	# print(request.POST)
# 	# print(request.GET)
# 	# print(request.GET['title']) 
# 	"""在url添加/?title=...,可獲得傳遞到server的資訊，但不建議此方法,會有安全問題"""

# 	# my_new_title = request.POST.get('title')
# 	# print(my_new_title)

# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 		# Product.objects.create(title=my_new_title) 
# 		""" 上一行不能在此用, 欄位不全, create時會出現錯誤"""

# 	context = {}
# 	return render(request, "products/product_create.html", context)

# 25 - Pure Django Form
# # @csrf_exempt # html中的<form></form>如果沒包含{% csrf_token %}
# def product_create_view(request):
# 	# my_form = RawProductForm()
# 	# my_form = RawProductForm(request.POST)

# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			# now the data is good
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)

# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "products/product_create.html", context)

"""27 Form Validation Methods (根據23修改)"""
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()  # 此行讓資料新增後，頁面會被reset(rerender the form)

	context = {
		'form': form
	}
	# 使用C:\Users\customer\dev\trydjango\src\products\templates\products中product_create.html
	return render(request, "products/product_create.html", context)

# 28
def render_initial_data(request):
	initial_data = {
		'title': "My this awesome title"
	}

	"""使用raw Django form"""
	# form = RawProductForm(request.POST or None, initial=initial_data) 
	"""使用 product form 也就是 Model form"""
	# form = ProductForm(request.POST or None, initial=initial_data)

	obj = Product.objects.get(id=1)
	# form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

# 29
def dynamic_lookup_view(request, my_id):
	obj = Product.objects.get(id=my_id)  # id=變數,這就有了動態樣式
	context = {
		"object": obj
	}
	return render(request, "products/product_detail.html", context)

# 30
def dynamic_lookup_view(request, my_id):
	# obj = Product.objects.get(id=my_id)
	# obj = get_object_or_404(Product, id=my_id) # 此法較好,執行較快

	# obj = Product.objects.get(id=my_id)
	try:
		obj = Product.objects.get(id=my_id)
	except Product.DoesNotExist:
		raise Http404 
	context = {
		"object": obj
	}
	return render(request, "products/product_detail.html", context)

# 31
def product_delete_view(request, my_id):
	obj = get_object_or_404(Product, id=my_id)
	# POST (DELETE) request
	if request.method == "POST":
		# confirming delete
		obj.delete()

		return redirect('../../../')
	context = {
		"object": obj
	}
	return render(request, "products/product_delete.html", context)

# 32
def product_list_view(request):
	queryset = Product.objects.all() #list of objects
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)

