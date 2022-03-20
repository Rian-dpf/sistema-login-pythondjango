from django.shortcuts import render
from django.contrib.auth.models import User

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