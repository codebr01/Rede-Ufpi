from django.urls import path
from app_rede_ufpi import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('redeufpi/login.html', views.login_view, name='login'),
    path('redeufpi/cadastro.html', views.cadastro, name='cadastro'),
]