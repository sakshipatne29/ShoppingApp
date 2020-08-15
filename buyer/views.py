from django.shortcuts import render, redirect
from seller.models import Product, Category
from ShoppingApp.models import UserProfile
from .models import Cart
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
@login_required
def home(request):
	pObjs = Product.objects.raw("select * from seller_product")
	catObjs = Category.objects.all()
	return render(request, 'WelcomeBuyer.html', {'data' : pObjs, 'cat' : catObjs})

@login_required
def cart(request, id):

	pObj = Product.objects.get(id=id)
	uObj = UserProfile.objects.get(user__username=request.user)
	url = "/buyer/home/"

	try:
		c = Cart(user_profile =uObj , product=pObj)
		c.save()
	except:
		return HttpResponse('<script>alert("Product is already added to your cart");\
			window.location="%s"</script>' %url)
	return HttpResponse('<script>alert("Product has been added to your cart");\
			window.location="%s"</script>' %url)
	#return redirect('/buyer/home/')

@login_required
def cartvalue(request):
	user = UserProfile.objects.get(user__username=request.user)
	p = Cart.objects.filter(user_profile_id=user.id)
	items = []
	for i in p:
		items.append(Product.objects.get(id=i.product_id))
	return render(request,'cartdetails.html',{'added_products' : items})



def cartcalculate(request):
	if request.method == 'POST':
		q = request.POST.getlist('productqty')
		pid = request.POST.getlist('pid')
		price = request.POST.getlist('price')
		sum = 0
		for i in range(len(q)):
			sum = sum + int(q[i]) * float(price[i])

			updateProduct = Product.objects.filter(id=pid[i])
			updateQty = updateProduct[0].qty-int(q[i])
			updateProduct.update(qty=updateQty)

		cartObjs = Cart.objects.filter(user_profile__user_id=request.user)
		cartObjs.delete()
			#use query of raw
		message = 'Your order is processed of {}'.format(sum)
		send_mail('Order details', message, 'sakshipatne206@gmail.com', ['patnesakshi206@gmail.com'] )
		return render(request,'checkout.html',{'data' : sum})

def deletecart(request, id):
	pObj = Product.objects.get(id=id)
	uObj = UserProfile.objects.get(user__username=request.user)
	c = Cart.objects.get(user_profile=uObj , product=pObj)
	c.delete()
	return redirect('/buyer/cartvalue/')



















































































