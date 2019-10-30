from django.db import models

# Create your models here.

class Coletor(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name= 'Nome'
    )
    cpf = models.CharField(
        max_length=11,
        verbose_name= 'CPF'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name= 'Email'
    )
    senha = models.CharField(
        max_length=255,
        verbose_name= 'Senha'
    )
    def __str__(self):
        return self.nome