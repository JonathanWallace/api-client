from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    rg = models.CharField(max_length=9, unique=True)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField()


    def __str__(self):
        return self.nome