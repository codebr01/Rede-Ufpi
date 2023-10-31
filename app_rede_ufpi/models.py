from django.db import models

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