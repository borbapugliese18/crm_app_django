from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.models import Record

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    records = Record.objects.all()

    
    return render(request, 'home.html', {'records':records})

def login_user(request):

    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request, 
            username=username,
            password=password
        )
        if usuario is not None:
            login(request, usuario)
            messages.success(request, "Login efetuado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

def customer_record(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    customer_record = Record.objects.get(id=pk)
    
    return render(request, 'record.html', {'customer_record':customer_record})
