from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect(reverse('cadastro') )  # Redirecione para a página de cadastro ou outra de sua escolha.
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
            return redirect(reverse('cadastro'))

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            messages.success(request, 'Login feito com sucesso')
            return redirect(reverse('gerenciar_exames'), next='/empresarial/gerenciar_clientes/')  # Redirecione para a página após o login ou outra de sua escolha.
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos')
            return redirect(reverse('login'))

        
