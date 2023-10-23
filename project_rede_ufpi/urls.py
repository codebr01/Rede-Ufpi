from django.urls import path
from app_rede_ufpi import views

urlpatterns = [
    path('', views.home, name='home'),
    path('redeufpi/login.html', views.login, name='login'),
    path('redeufpi/cadastro.html', views.cadastro, name='cadastro')
]
