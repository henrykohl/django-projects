from django.db import models

from django.urls import reverse # 節34

# Create your models here.
class Product(models.Model):
	# title       = models.TextField()
	title       = models.CharField(max_length=120) # max_length is required
	# description = models.TextField()
	description = models.TextField(blank=True, null=True)
	# price       = models.TextField()
	price       = models.DecimalField(decimal_places=2, max_digits=1000)
	# summary     = models.TextField(default='this is cool!')
	# summary     = models.TextField()
	summary     = models.TextField(blank=False, null=False)
    # null=False 意味著，欄位內容是必要的

	# featured    = models.BooleanField() # null=True,或 default=True 或都有
	# null=True的作用, 在python manage.py makemigrations時, 錯誤警告提示

	featured    = models.BooleanField(default=True)

	def get_absolute_url(self):
		# print(self.title)
		# return f"/products/{self.id}/" # 節33
		# print(reverse("product-detail")) # 不能用
		# print(reverse("product-detail", kwargs={"my_id": self.id}))
		# return reverse("product-detail", kwargs={"my_id": self.id})        # 節34
		return reverse("products:product-detail", kwargs={"my_id": self.id}) # 節35 #f"/products/{self.id}/"