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
    path('redeufpi/comunidades.html', views.comunidades, name='comunidades'),
    path('redeufpi/home-page.html', views.home_page, name='home-page'),
    path('redeufpi/post.html', views.post, name='post'),
    path('logout/', views.logout_view, name='logout'),
    path('redeufpi/criar-comunidade.html', views.criar_comunidade, name='criar-comunidade'),
]