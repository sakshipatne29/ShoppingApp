from django.db import models
from ShoppingApp.models import UserProfile
# Create your models here.
class Category(models.Model):
	catname = models.CharField(max_length=30)



class Product(models.Model):
	name = models.CharField(max_length=40)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	des = models.CharField(max_length=100)
	qty = models.IntegerField()
	pro_image = models.ImageField(upload_to="productimage", null=True)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	added_by = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)