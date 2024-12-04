from django.contrib.auth import authenticate, login 
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User 
from .models import Task
from .forms import TaskForm

def login_view(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)

       if user is not None:
            login(request, user)
            return redirect('list')
       else:
            return render(request, 'login/index.html', {'error': 'Credenciais inválidas'})   

    return render(request, 'login/index.html')

def tasklist_view(request):
    tasks = Task.objects.filter(user=request.user) 
    return render(request, "tasklist/index.html", {"tasks": tasks})

def taskAdd_view(request):
        
    if request.method == "POST":
            
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")

        Task.objects.create(
            user=request.user,
            title=title,
            due_date=due_date,
            priority=priority,
        )
            
        return redirect("list")
    return render(request,'taskAdd/index.html')

def cadastro_view(request): 
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("reg")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Usuário registrado com sucesso! Faça login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Erro ao registrar usuário: {e}")
            return redirect("reg")           
    return render(request, 'cadastro/index.html')    

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('list') 

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
          form.save()
        return redirect('list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskedit/index.html', {'form': form, 'task': task})    