from django.db import models


class Product(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 100)
	price = models.FloatField()
	category_id = models.IntegerField()

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Tовары"
class Category(models.Model):
	category_id = models.IntegerField()
	name = models.CharField (max_length = 100)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

class Order(models.Model):
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	comment = models.TextField()
	status = models.BooleanField(default = False)
	
	def __str__(self):
		return self.name + ' ' + str(self.status)
	class Meta:
		verbose_name = "Заказ" 
		verbose_name_plural = "Заказы"


