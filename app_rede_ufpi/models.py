from django.db import models
from django.contrib.auth import get_user_model

class User(models.Model):

    email = models.CharField(
        max_length=255
    )
    senha = models.CharField(
        max_length=100
    )
    matricula = models.CharField(
        max_length=11
    )


class MainPost(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    conteudo = models.TextField()

    user = models.ForeignKey(
        get_user_model() , 
        on_delete=models.CASCADE
    )

class Comunidades(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    nome = models.CharField(
        max_length=255
    )

    user = models.ForeignKey(
        get_user_model() ,
        on_delete=models.CASCADE
    )

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    conteudo = models.TextField()
    comunidade = models.ForeignKey(
        'Comunidades',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )