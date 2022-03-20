from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def Home(request):
    return render(request, 'home.html')

def Create(request):
    return render(request, 'create.html')

def Store(request): # Inserção dos dados dos usuário no banco

    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senhas diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'

    return render(request, 'create.html', data)

def Painel(request): #Formulário do painel de login
    return render(request, 'painel.html')

def Login(request): #Processar o login
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request,user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário e ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

def dashboard(request): #Página inicial do dashboard
    return render(request, 'dashboard/home.html')