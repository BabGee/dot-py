from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=120)
	price = models.IntegerField()
	
	def __str__(self):
		return self.name

# class Order(models.Model):
	# ref_code = models.CharField(max_length=120)
	# owner = models.ForeignKey(Profile, on_delete=models.Set_Null, null=True)
	# is_ordered = models.BooleanField(default=False)
	# items = models.ManyToManyField(order_item)
	# date_ordered = models.DateTimeField(auto_now=True)
	
	# def get_cart_items(self):
		# return self.items.all()
		
	# def get_cart_total(self):
		# return sum([item.product.price for items in self.items.all()])

	# def __str__(self):
		# return "{0} {1}".format(self.owner, self.ref_code)