import pytest
from django.urls import reverse
from app_produtos.models import CadastrarColaborador  

@pytest.mark.django_db
def test_cadastrar_colaborador(client):
   
    nome_colaborador = "Carlos Silva"
    cpf = "123.456.789-10"
    cargo = "Eletricista"
    setor = "Eletricista"
    
    
    cadastro_url = reverse('cadastrar_colaborador')  

    
    response = client.post(cadastro_url, {
        'nome_colaborador': nome_colaborador,
        'cpf': cpf,
        'cargo': cargo,
        'setor': setor,
    })

        
    assert response.status_code == 200  
    assert "Colaborador cadastrado com sucesso!" in response.content.decode()  

    # Verificar se o colaborador foi realmente adicionado ao banco de dados
    colaborador = CadastrarColaborador.objects.filter(cpf=cpf).first()
    assert colaborador is not None
    assert colaborador.nome_colaborador == nome_colaborador
    assert colaborador.cpf == cpf
    assert colaborador.cargo == cargo
    assert colaborador.setor == setor

    print(f"Resultado: Colaborador cadastrado com sucesso!")
    

@pytest.mark.django_db
def test_cadastrar_colaborador_incompleto(client):
    
    cadastro_url = reverse('cadastrar_colaborador')
    
    
    response = client.post(cadastro_url, {
        'nome_colaborador': 'Carlos Silva',
        'cpf': '123.456.789-10',
        'cargo': '',  
        'setor': 'Eletricista',
    })
    
    assert response.status_code == 200
    
    assert "Colaborador não foi cadastrado. Preencher o campo: cargo" in response.content.decode()

    # Garantir que nenhum colaborador foi cadastrado no banco de dados
    colaborador = CadastrarColaborador.objects.filter(cpf='123.456.789-10').first()
    assert colaborador is None

    print("Teste de formulário incompleto executado com sucesso.")

@pytest.mark.django_db
def test_atualizar_colaborador_sucesso(client):
    
    colaborador = CadastrarColaborador.objects.create(
        nome_colaborador="Carlos Silva",
        cpf="123.456.789-10",
        cargo="Eletricista",
        setor="Eletricista",
    )

    
    editar_url = reverse('editar_colaborador', args=[colaborador.id])

    
    response = client.post(editar_url, {
        'nome_colaborador': "Carlos Eduardo Silva",
        'cpf': "123.456.789-10",
        'cargo': "Analista Sênior",
        'setor': "Financeiro",
    }, follow=True)
    
    assert response.status_code == 200 
    assert "Colaborador atualizado com sucesso!" in response.content.decode()

    # Verificar se os dados do colaborador foram atualizados no banco de dados
    colaborador.refresh_from_db()
    assert colaborador.nome_colaborador == "Carlos Eduardo Silva"
    assert colaborador.cpf == "123.456.789-10"
    assert colaborador.cargo == "Analista Sênior"
    assert colaborador.setor == "Financeiro"

    print("Teste de atualização bem-sucedida executado com sucesso.")


@pytest.mark.django_db
def test_excluir_colaborador_com_sucesso(client):
    
    colaborador = CadastrarColaborador.objects.create(
        nome_colaborador="Carlos Silva",
        cpf="123.456.789-10",
        cargo="Eletricista",
        setor="Eletricista",
    )

    
    deletar_url = reverse('deletar_colaborador', args=[colaborador.id])

    
    response = client.post(deletar_url, follow=True)

    
    assert response.status_code == 200 
    assert "Colaborador excluído com sucesso!" in response.content.decode()  

    # Verificar se o colaborador foi realmente excluído do banco de dados
    colaborador_excluido = CadastrarColaborador.objects.filter(id=colaborador.id).first()
    assert colaborador_excluido is None  # O colaborador não deve existir mais no banco de dados

    print("Colaborador excluido com sucesso.")