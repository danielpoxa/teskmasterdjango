from django.contrib.auth import authenticate, login 
from django.shortcuts import render, redirect


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
    return render(request, 'tasklist/index.html')

def taskAdd_view(request):
    return render(request,'taskAdd/index.html')