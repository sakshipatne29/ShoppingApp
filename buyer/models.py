from django.db import models
from ShoppingApp.models import UserProfile
from seller.models import Product
# Create your models here.
class Cart(models.Model):
	class Meta():
		unique_together = (('user_profile', 'product'))
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
