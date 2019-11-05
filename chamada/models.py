from django.db import models

# Create your models here.

class Chamada(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name= 'Nome'
    )
    cep = models.CharField(
        max_length=8,
        verbose_name='CEP'
    )
    bairro = models.CharField(
        max_length=255,
        verbose_name='Bairro'
    )
    endereco = models.CharField(
        max_length=255,
        verbose_name= 'Endereço'
    )
    numero = models.CharField(
        max_length=255,
        verbose_name= 'Numero'
    )
    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento'
    )
    telefone = models.CharField(
        max_length=255,
        verbose_name= 'Telefone'
    )
    descricao = models.CharField(
        max_length=255,
        verbose_name='Descrição'
    )

    def __str__(self):
        return self.nome