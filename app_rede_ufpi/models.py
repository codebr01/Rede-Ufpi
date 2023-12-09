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