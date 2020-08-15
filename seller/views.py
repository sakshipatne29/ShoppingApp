from django.shortcuts import render, redirect
from .models import Category, Product
from ShoppingApp.models import UserProfile
# Create your views here.

def home(request):
	return render(request, 'WelcomeSeller.html')


def addproduct(request):
	catObjs = Category.objects.all()

	if request.method =="POST":
		pname = request.POST['pname']
		price = request.POST['price']
		qty  = request.POST['qty']
		des = request.POST['des']
		pic = request.FILES['pic']

		catobj = Category.objects.get(id=request.POST['cid'])
		userobj = UserProfile.objects.get(user__username=request.user)
		p = Product(name=pname, pro_image=pic, price=price, des=des, qty=qty, category=catobj, added_by=userobj)
		p.save()
		return redirect('/seller/addproduct/')

	return render(request, 'addproduct.html', {'cats' : catObjs})