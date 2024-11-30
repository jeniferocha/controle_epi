import pytest
from django.urls import reverse
from app_produtos.models import CadastrarEquipamento  

@pytest.mark.django_db
def test_cadastrar_equipamento(client):
    
    cod_equipamento = 123456
    nome_equipamento = "Capa de proteção"
    
    cadastro_url = reverse('cadastrar_equipamento')  
   
    response = client.post(cadastro_url, {
        'cod_equipamento': cod_equipamento,
        'nome_equipamento': nome_equipamento,
    })
    
    assert response.status_code == 200  
    assert "Equipamento cadastrado com sucesso!" in response.content.decode() 


    equipamento = CadastrarEquipamento.objects.filter(cod_equipamento=cod_equipamento).first()
    assert equipamento is not None
    assert equipamento.cod_equipamento == cod_equipamento
    assert equipamento.nome_equipamento == nome_equipamento

    print("Resultado: Equipamento cadastrado com sucesso!")


 
@pytest.mark.django_db
def test_cadastrar_equipamento_incompleto(client):
    
    cadastro_url = reverse('cadastrar_equipamento')
    
    response = client.post(cadastro_url, {
        'cod_equipamento': 123456,
        'nome_equipamento': '',
    })
    
    assert response.status_code == 200
    
    assert "Equipamento não foi cadastrado. Preencher o campo: nome_equipamento" in response.content.decode()
   
    equipamento = CadastrarEquipamento.objects.filter(cod_equipamento=123456).first()
    assert equipamento is None

    print("Teste de formulário incompleto executado com sucesso.")