from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = ('mobile','role')

class UserModelForm(forms.ModelForm):
	class Meta():
		model = User
		#fields = '__all__'
		fields = ('username', 'password', 'email')