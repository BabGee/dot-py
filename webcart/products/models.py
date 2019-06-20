from django.db import models

class Product(models.Model):
	#image = models.ImageField(default="food.jpg", upload_to="food_pics")
	title = models.CharField(max_length=120)
	price = models.IntegerField()

	def __str__(self):
		return self.title
