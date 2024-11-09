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
    colaborador_id = models.ForeignKey(CadastrarColaborador, on_delete=models.CASCADE, null=True)
    equipamento_id = models.ForeignKey(CadastrarEquipamento, on_delete=models.CASCADE, null=True)
    data_emprestimo = models.DateField()
    data_prevista_devolucao = models.DateField()
    status = models.CharField(max_length=100)
    condicoes = models.CharField(max_length=100)  
    data_devolucao = models.DateField(null=True, blank=True)
    observacao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        base_str = f"Colaborador: {self.colaborador_id} - Equipamento: {self.equipamento_id} - Data_emprestimo: {self.data_emprestimo} - Data_prevista_devolução: {self.data_prevista_devolucao} - Status: {self.status} - Condições: {self.condicoes}"
        
        # Adiciona 'data_devolucao' e 'observacao' se existirem
        if self.data_devolucao:
            base_str += f" - Data_devolução: {self.data_devolucao}"
        if self.observacao:
            base_str += f" - Observação: {self.observacao}"
        
        return base_str


class cadastrarLogin(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=140)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):  
        return f"Nome: {self.nome} - Email: {self.email} - Username: {self.username} - Password: {self.password}"   


   