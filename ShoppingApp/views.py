from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import UserProfile

def signup(request):
	u1 = UserModelForm()
	u2 = UserProfileForm()
	
	if request.method == "POST":
		u1 = UserModelForm(request.POST)
		u2 = UserProfileForm(request.POST)
		
		if u1.is_valid() and u2.is_valid():
			u1Saved = u1.save()	
			u1Saved.set_password(u1Saved.password)
			u1Saved.save()

			u2Saved = u2.save(commit=False)
			u2Saved.user = u1Saved
			u2Saved.save()
			return redirect('/signup/')


	data = {'f1':u1, 'f2':u2}
	return render(request, 'signup.html', data)

def login_call(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		selectedUser = authenticate(username=username, password=password)

		if selectedUser:
			login(request, selectedUser)
			uData = UserProfile.objects.get(user__username=request.user)
			if uData.role == 'buyer':
				return redirect('/buyer/home/')
			elif uData.role == 'seller':
				return redirect('/seller/home/')
			#return redirect('/welcome/')
		else:
			return HttpResponse("<h1>Invalid User</h1>")


	return render(request, 'login.html')

@login_required
def logout_call(request):
	logout(request)
	return redirect('/login/')

@login_required	
def welcome(request):
	return render(request, 'welcome.html')


def part1Font(request):
	return render(request, 'part1Fonts.html')