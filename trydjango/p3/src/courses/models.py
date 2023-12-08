from django.db import models # default

from django.urls import reverse # 自行新增

# Create your models here.
class Course(models.Model): # 41 
	title = models.CharField(max_length=120)

	"""自行新增"""
	def get_absolute_url(self):
		return reverse("courses:courses-detail", kwargs={"id": self.id})