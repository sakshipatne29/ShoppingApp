from django.urls import path
from . import views

app_name = 'buyer'

urlpatterns = [
	path('home/', views.home),	
	path('cart/<int:id>/', views.cart, name="addcart"),
	path('cartvalue/', views.cartvalue),
	path('cartcalculate/', views.cartcalculate),
	path('deletecart/<int:id>/', views.deletecart, name="deletecart")
]