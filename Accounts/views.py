from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				messages.success(request,('Username has already been taken!'))
				return render(request,'Accounts/signup.html')
			except User.DoesNotExist:
				user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			messages.success(request,('Passwords Must Match'))
			return render(request,'Accounts/signup.html')
	else:
		return render(request,'Accounts/signup.html')

def login(request):
	if request.method == 'POST':
		user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.success(request,('Username or Password is incorrect'))
			return render(request,'Accounts/login.html')

	else:
		return render(request,'Accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')