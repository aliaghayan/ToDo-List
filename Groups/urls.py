from django.urls import path , include
from . import views

urlpatterns = [
	path('',views.home,name='home'),
    path('create',views.Create,name='create'),
    path('add_task',views.add_task,name='add_task'),
]
    # path('<int:Groups_id>',views.tasks,name='tasks'),