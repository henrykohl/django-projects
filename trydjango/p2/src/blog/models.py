from django.db import models

from django.urls import reverse

# Create your models here.
class Article(models.Model):
	title   = models.CharField(max_length=120)
	content = models.TextField()
	active  = models.BooleanField(default=True)

	def get_absolute_url(self):
		# print(self)    # 印出Article object (數字)
		# print(self.id) # 印出`數字'
		return reverse("articles:article-detail",kwargs={"pk": self.id})
	# """reverse function is going to the detail view"""	