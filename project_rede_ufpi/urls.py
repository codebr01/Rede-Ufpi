from django.urls import path
from app_rede_ufpi import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('redeufpi/login.html', views.login, name='login'),
    path('redeufpi/cadastro.html', views.cadastro, name='cadastro'),
]