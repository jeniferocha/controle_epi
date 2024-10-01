from django.db import models

class CadastrarEquipamento(models.Model):
    cod_equipamento = models.IntegerField()
    nome_equipamento = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Codigo: {self.cod_equipamento} - Nome: {self.nome_equipamento}"



class CadastrarColaborador(models.Model):    
    nome_colaborador = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Nome: {self.nome_colaborador} - Cpf: {self.cpf} - Cargo: {self.cargo} - Setor: {self.setor}"