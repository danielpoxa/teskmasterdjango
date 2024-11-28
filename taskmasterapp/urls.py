from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),   
    path('list/', views.tasklist_view, name='list'),
    path('add/', views.taskAdd_view, name='add') 
]
