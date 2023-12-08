from django.shortcuts import render, get_object_or_404, redirect # default # 41 # 46
from django.views import View

from .forms import CourseModelForm
from .models import Course # 41

# Create your views here.

# BASE VIEW CLass = VIEW

# 47
# class CourseObjectMixin(object):
# 	model = Course
# 	# lookup = 'id' # 方法一
# 	def get_object(self):
# 		# id = self.kwargs.get(self.lookup) # 方法一
# 		id = self.kwargs.get('id')          # 方法二
# 		obj = None 
# 		if id is not None:
# 			obj = get_object_or_404(self.model, id=id)
# 		return obj 

# 47
# class CourseDeleteView(CourseObjectMixin, View):
# 	template_name = "courses/course_delete.html"

# 	def get(self, request, id=None, *args, **kwargs): 
# 		# GET method
# 		context = {}
# 		obj = self.get_object()
# 		if obj is not None:
# 			context['object'] = obj
# 		return render(request, self.template_name, context)

# 	def post(self, request, id=None, *args, **kwargs):
# 		# POST method
# 		context = {}
# 		obj = self.get_object()
# 		if obj is not None:
# 			obj.delete()
# 			context['object'] = None
# 			return redirect('/courses/')
# 		return render(request, self.template_name, context)


class CourseDeleteView(View):
	template_name = "courses/course_delete.html"
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id)
		return obj 

	def get(self, request, id=None, *args, **kwargs): 
		# GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			return redirect('/courses/')
		return render(request, self.template_name, context)


# class CourseUpdateView(CourseObjectMixin, View): # 47
class CourseUpdateView(View):
	template_name = "courses/course_update.html"
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			# context['object'] = obj 不需要
		return obj 

	def get(self, request, id=None, *args, **kwargs): # `id=None' means `id is no longer required
		"""注意:get函數裡可以直接調取到id,或是用self.kwargs.get('id')取得id"""
		context = {}
		obj = self.get_object()
		if id is not None:
			form = CourseModelForm(instance=obj)
			context['object'] = obj   # 原始內容
			context['form'] = form    # 可更改的欄位
		# context = {'object': self.get_object()}
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		form = CourseModelForm(request.POST, instance=obj)
		if obj is not None:
			if form.is_valid():
				form.save()
		"""下兩行是在按下save後才會顯出效果"""
		context['object'] = obj    # 更改後內容
		context['form'] = form     # 可更改的欄位
		# context = {}
		return render(request, self.template_name, context)

class CourseCreateView(View):
	template_name = "courses/course_create.html"
	def get(self, request, *args, **kwargs):
		# GET method
		form = CourseModelForm()
		context = {"form": form}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		# POST method
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseModelForm()
		context = {"form": form}
		# context = {}
		return render(request, self.template_name, context)

class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class MyListView(CourseListView):        
	queryset = Course.objects.filter(id=2)




# class CourseView(CourseObjectMixin, View): # 47
# 	template_name = "courses/course_detail.html"
# 	def get(self, request, id=None, *args, **kwargs):
# 		# GET method
# 		context = {'object': self.get_object()}
# 		return render(request, self.template_name, context)

class CourseView(View):
	# def get(self, request, *args, **kwargs):
	# 	return render(request, 'about.html', {})
	template_name = "courses/course_detail.html" # DetailView
	def get(self, request, id=None, *args, **kwargs): # `id=None' means `id is no longer required
		context = {}
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			context['object'] = obj
		"""需要定義get_object()"""
		# context = {'object': self.get_object()}
		return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})


