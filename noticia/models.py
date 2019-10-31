from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(
        max_length=255,
        verbose_name= 'Nome'
    )
    noticia = models.CharField(
        max_length=255,
        verbose_name= 'Noticia'
    )
    def __str__(self):
        return self.titulo