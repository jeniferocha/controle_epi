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


class RegistrarAcao(models.Model):
    nome_colaborador = models.CharField(max_length=100)
    nome_equipamento = models.CharField(max_length=100)
    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    status = models.CharField(max_length=100)
    condicoes = models.CharField(max_length=100)

    def __str__(self):
        return f"Colaborador: {self.nome_colaborador} - Equipamento: {self.nome_equipamento} - Data_emprestimo: {self.data_emprestimo} - Data_prevista_devolução: {self.data_prevista_devolucao} - Status: {self.status} - Condições: {self.condicoes}"

class ColaboradorEquipamento(models.Model):
    colaborador_id = models.ForeignKey(CadastrarColaborador, on_delete=models.CASCADE)
    equipamento_id = models.ForeignKey(CadastrarEquipamento, on_delete=models.CASCADE)
    data_emprestimo_id = models.ForeignKey(RegistrarAcao, on_delete=models.CASCADE)


   