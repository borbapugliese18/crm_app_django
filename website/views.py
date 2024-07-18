from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.models import Record
from website.forms import AddRecordForm

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

def delete_record(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    delete_it = Record.objects.get(id=pk)
    delete_it.delete()

    messages.success(request, "Record deletado com sucesso!")
    return redirect('home')

def add_record(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record salvo com sucesso!")
            return redirect('home')
        
    return render(request, 'add_record.html', {'form':form})

def update_record(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Record alterado com saucesso!")
            return redirect('home')
        
    return render(request, 'update_record.html', {'form':form})
    