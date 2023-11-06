from django.shortcuts import render, redirect
from .models import User

def home(request):
  return render(request, 'redeufpi/home.html')

def login(request):

  users = User.objects.all()
  
  if request.method == 'POST':
    for user in users:
      if request.POST.get('email') == user.email and request.POST.get('senha') == user.senha:
        return render(request, 'redeufpi/tela_inicial.html', {'user':user})
    return render(request, 'redeufpi/login.html')
  else:
    return render(request, 'redeufpi/login.html')

def cadastro(request):

  if request.method == 'POST':
    novo_usuario = User()

    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.matricula = request.POST.get('matricula')

    novo_usuario.save()

    return redirect('/')
  else:
    return render(request, 'redeufpi/cadastro.html')