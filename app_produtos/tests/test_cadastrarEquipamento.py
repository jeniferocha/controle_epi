import pytest
from django.urls import reverse
from app_produtos.models import CadastrarEquipamento


@pytest.mark.django_db
def test_cadastrar_equipamento_sucesso(client):
    
    cod_equipamento = "9245"
    nome_equipamento = "Equipamento teste"

    cadastro_url = reverse('cadastrar_equipamento')  
        
    response = client.post(cadastro_url, {
        'cod_equipamento': cod_equipamento,
        'nome_equipamento': nome_equipamento,
    })

    assert response.status_code == 200  
    assert "Equipamento cadastrado com sucesso!" in response.content.decode()  

    # Verificar se o equipamento foi realmente adicionado ao banco de dados
    equipamento = CadastrarEquipamento.objects.filter(cod_equipamento=cod_equipamento).first()
    assert equipamento is not None
    assert equipamento.cod_equipamento == cod_equipamento
    assert equipamento.nome_equipamento == nome_equipamento
     