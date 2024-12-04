from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),   
    path('list/', views.tasklist_view, name='list'),
    path('add/', views.taskAdd_view, name='add'),
    path('reg/', views.cadastro_view,name='reg'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
