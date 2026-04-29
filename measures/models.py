from django.db import models
from django.contrib.auth.models import User

class Measures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name= 'Altura')
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name= 'Peso')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering=['created_at']
        verbose_name = 'Medida'
