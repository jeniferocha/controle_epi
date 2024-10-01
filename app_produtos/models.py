from django.db import models

class CadastrarEquipamento(models.Model):
    cod_equipamento = models.IntegerField()
    nome_equipamento = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Codigo: {self.cod_equipamento} - Nome: {self.nome_equipamento}"