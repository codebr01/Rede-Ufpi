from django.shortcuts import render

def home(request):
  return render(request, 'redeufpi/home.html')

def login(request):
  return render(request, 'redeufpi/login.html')

def cadastro(request):
  return render(request, 'redeufpi/cadastro.html')