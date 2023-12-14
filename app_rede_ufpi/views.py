from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import MainPost
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'redeufpi/login.html')

def login_view(request):
    error_message = ''
    if request.method == 'POST':

        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        user = authenticate(request, username=matricula, password=senha)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            error_message = 'Matrícula ou senha inválidos'
            return render(request, 'redeufpi/login.html', {'error_message':error_message})
    else:
        return render(request, 'redeufpi/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.create_user(username=matricula, password=senha, email=email)
        user.save()
        return login_view(request)
    else:
        return render(request, 'redeufpi/cadastro.html')

@login_required    
def comunidades(request):
    return render(request, 'redeufpi/comunidades.html')

@login_required
def home_page(request):

    posts_list = MainPost.objects.all()
    
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'redeufpi/home-page.html', {'posts':posts})

@login_required
def post(request):
    error_message = ''
    if request.method == 'POST' and request.user.is_authenticated:
        conteudo = request.POST.get('conteudo')
        if conteudo != '':
            post = MainPost.objects.create(conteudo=conteudo, user=request.user)
            post.save()
            return redirect('home-page')
        else:
            error_message = 'Não é possível criar um post vazio'
            posts_list = MainPost.objects.all()
            paginator = Paginator(posts_list, 4)
            page = request.GET.get('page')
            posts = paginator.get_page(page)
            return render(request, 'redeufpi/home-page.html', {'error_message':error_message, 'posts':posts})
    else:
        return redirect('login')