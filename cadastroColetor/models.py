from django.db import models

# Create your models here.

class Coletor(models.Model):
    BAIRRO = (
        ("Centro","Centro"),
        ("Laranjeiras","Laranjeiras"),
        ("Nova Era","Nova Era"),
        ("Nova Caieiras","Nova Caieiras"),
        ("Serpa","Serpa"),
    )

    nome = models.CharField(
        max_length=255,
        verbose_name= 'Nome'
    )
    cpf = models.CharField(
        max_length=11,
        verbose_name= 'CPF'
    )
    bairro = models.CharField(
        choices=BAIRRO, 
        max_length=255,
        verbose_name='Bairro de atuação'
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