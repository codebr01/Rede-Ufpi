from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import MainPost, Comunidades, Post, Comentario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import ComentarioForm

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
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.create_user(username=matricula, password=senha, email=email, first_name=nome, last_name=sobrenome)
        user.save()
        return login_view(request)
    else:
        return render(request, 'redeufpi/cadastro.html')

@login_required
def home_page(request):

    posts_list = MainPost.objects.all().order_by('-data')
    comunidades = Comunidades.objects.all()
    user = request.user
    
    paginator = Paginator(posts_list, 9999)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'redeufpi/home-page.html', {'posts':posts, 'comunidades':comunidades, 'user':user})

@login_required
def post(request):
    error_message = ''
    if request.user.is_authenticated:
        if request.method == 'POST':
            conteudo = request.POST.get('conteudo')
            if conteudo != '':
                post = MainPost.objects.create(conteudo=conteudo, user=request.user)
                post.save()
                return redirect('home-page')
            else:
                error_message = 'Não é possível criar um post vazio'
                messages.error(request, error_message)
                # posts_list = MainPost.objects.all()
                # paginator = Paginator(posts_list, 4)
                # page = request.GET.get('page')
                # posts = paginator.get_page(page)
                return redirect('home-page')
    else:
        return redirect('login')
    
@login_required
def postagem(request, id):
    post = MainPost.objects.get(id=id)
    user = request.user
    comments = Comentario.objects.filter(main_post=post)
    return render(request, 'redeufpi/post.html', {'post':post, 'user':user, 'comments': comments})

@login_required
def perfil(request, username):

    user = User.objects.get(username=username)
    posts = MainPost.objects.filter(user=user).order_by('-data')

    return render(request, 'redeufpi/perfil.html', {'user':user, 'posts':posts})

@login_required
def editar_perfil(request):
    return render(request, 'redeufpi/editar.html')

@login_required
def comunidade(request, name):

    comunidades = Comunidades.objects.all()
    comunidade = Comunidades.objects.get(nome=name)
    posts_list = Post.objects.filter(comunidade=comunidade).order_by('-data')

    paginator = Paginator(posts_list, 9999)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'redeufpi/comunidade.html', {'comunidade':comunidade, 'comunidades':comunidades, 'posts':posts})

@login_required
def criar_comunidade(request):
    if request.method == 'POST':
        nome = request.POST.get('nome-comunidade')
        if nome != '':
            comunidade = Comunidades.objects.create(nome=nome, user=request.user)
            comunidade.save()
            return redirect('home-page')
        else:
            error_message = 'Não é possível criar uma comunidade sem nome'
            return render(request, 'redeufpi/criar-comunidade.html', {'error_message':error_message})
    else:
        return render(request, 'redeufpi/criar-comunidade.html')

@login_required
def comunidade_criar_post(request, name):
    error_message = ''
    if request.user.is_authenticated:
        if request.method == 'POST':
            conteudo = request.POST.get('conteudo')
            comunidade = Comunidades.objects.get(nome=name)
            if conteudo != '':
                post = Post.objects.create(conteudo=conteudo, user=request.user, comunidade=comunidade)
                post.save()
                return redirect('comunidade', name=comunidade.nome)
            else:
                error_message = 'Não é possível criar um post vazio'
                messages.error(request, error_message)
                return redirect('comunidade', name=comunidade.nome)
    else:
        return redirect('login')

@login_required    
def comunidades(request):
    comunidades = Comunidades.objects.all()
    return render(request, 'redeufpi/comunidades.html', {'comunidades':comunidades})

@login_required
def criar_comentario_main(request, post_id):
    post = get_object_or_404(MainPost, id=post_id)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = request.user
            comentario.main_post = post
            comentario.save()
            
            messages.success(request, 'Comentário postado com sucesso!')
            return redirect('postagem', id=post.id)
        else:
            messages.error(request, 'Erro ao postar o comentário. Verifique o formulário.')
    else:
        form = ComentarioForm()

    return render(request, 'post.html', {'post': post, 'form': form})