from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Group
from django.utils import timezone
def home(request):
    return render(request,'Groups/home.html')

@login_required
def Create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['description'] and request.FILES['icon']:
			group = Group()
			group.name = request.POST['title']
			group.description = request.POST['description']
			group.icon = request.FILES['icon']
			group.pub_date = timezone.datetime.now()
			group.created_by = request.user
			group.save()
			return redirect('home')
	else:
		messages.success(request,('All fields are required.'))
		return render(request, 'Groups/create.html')

    # return render(request,'Groups/create.html')