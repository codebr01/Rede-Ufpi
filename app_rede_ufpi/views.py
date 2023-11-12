from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'redeufpi/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return render(request, 'redeufpi/tela_inicial.html', {'user':user})
        else:
            return render(request, 'redeufpi/login.html')
    else:
        return render(request, 'redeufpi/login.html')

def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        matricula = request.POST.get('matricula')
        user = User.objects.create_user(username=matricula, password=senha, email=email)
        user.save()
        return redirect('/')
    else:
        return render(request, 'redeufpi/cadastro.html')