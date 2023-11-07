from django.urls import path
from app_rede_ufpi import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('redeufpi/login.html', views.login_view, name='login'),
    path('redeufpi/cadastro.html', views.cadastro, name='cadastro'),
]