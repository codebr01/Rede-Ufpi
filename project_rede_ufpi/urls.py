from django.urls import path
from app_rede_ufpi import views 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('redeufpi/login', views.login_view, name='login'),
    path('redeufpi/cadastro', views.cadastro, name='cadastro'),
    path('redeufpi/comunidades', views.comunidades, name='comunidades'),
    path('redeufpi/home-page', views.home_page, name='home-page'),
    path('redeufpi/post', views.post, name='post'),
    path('logout/', views.logout_view, name='logout'),
    path('redeufpi/criar-comunidade', views.criar_comunidade, name='criar-comunidade'),
    path('redeufpi/perfil/<int:username>', views.perfil, name='perfil'),
    path('redeufpi/comunidade/<str:name>', views.comunidade, name='comunidade'),
    path('redeufpi/comunidade/<str:name>/criar-post', views.comunidade_criar_post, name='criar-post'),
    path('redeufpi/editar-perfil', views.editar_perfil, name='editar-perfil'),
    path('redeufpi/post/<int:id>', views.postagem, name='post-public'),
    path('redeufpi/post/<int:post_id>/', views.criar_comentario_main, name='criar_comentario_main'),
    path('postagem/<int:id>/', views.postagem, name='postagem'),
    path('redeufpi/comunidade/post/<int:id>', views.comunidade_postagem, name='comunidade-post-public'),
    path('redeufpi/comunidade/post/<int:post_id>', views.criar_comentario, name='criar_comentario'),
    path('comunidade_postagem<int:id>/', views.comunidade_postagem, name='comunidade_postagem'),
]
