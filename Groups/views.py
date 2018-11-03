from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Group ,Todo
from django.utils import timezone
from .forms import TodoForm
from django.views.decorators.http import require_POST

def home(request):
	ggroups = Group.objects
	ttasks = Todo.objects
	return render(request,'Groups/home.html',{'ggroups':ggroups},{'ttasks':ttasks})


@login_required(login_url="/accounts/signup")
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
@login_required
def add_task(request):
    if request.method == 'POST':
    	if request.POST['text'] and request.POST['assigned_to']:
    		taskss = Todo()
    		taskss.text = request.POST['text']
    		taskss.assigned_to = request.POST['assigned_to']
    		taskss.save()
    		return redirect('home')
    	else:
    		messages.success(request,('All fields are required.'))
    		return render(request, 'Groups/home.html')
