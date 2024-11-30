import pytest
from django.urls import reverse
from app_produtos.models import CadastrarColaborador  

@pytest.mark.django_db
def test_cadastrar_colaborador(client):
    # Definir dados para o novo colaborador
    nome_colaborador = "Carlos Silva"
    cpf = "123.456.789-10"
    cargo = "Eletricista"
    setor = "Eletricista"
    
    # Passo 1: Acessar a tela de cadastro de colaboradores
    cadastro_url = reverse('cadastrar_colaborador')  

    # Passo 2: Preencher todos os campos obrigatórios
    response = client.post(cadastro_url, {
        'nome_colaborador': nome_colaborador,
        'cpf': cpf,
        'cargo': cargo,
        'setor': setor,
    })

    # Passo 3: Verificar se o colaborador foi cadastrado com sucesso
    # O sistema deve exibir uma mensagem de sucesso e permanecer na tela de cadastro
    assert response.status_code == 200  # A página não deve ser redirecionada, apenas re-renderizada
    assert "Colaborador cadastrado com sucesso!" in response.content.decode()  # Verificar a mensagem de sucesso

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
    # Definir URL do cadastro de colaboradores
    cadastro_url = reverse('cadastrar_colaborador')
    
    # Dados incompletos (faltando o campo 'cargo')
    response = client.post(cadastro_url, {
        'nome_colaborador': 'Carlos Silva',
        'cpf': '123.456.789-10',
        'cargo': '',  # Campo obrigatório vazio
        'setor': 'Eletricista',
    })
    
    # Verificar se a resposta HTTP foi bem-sucedida (re-renderização da página)
    assert response.status_code == 200

    # Verificar se a mensagem de erro foi exibida corretamente
    assert "Colaborador não foi cadastrado. Preencher o campo: cargo" in response.content.decode()

    # Garantir que nenhum colaborador foi cadastrado no banco de dados
    colaborador = CadastrarColaborador.objects.filter(cpf='123.456.789-10').first()
    assert colaborador is None

    print("Teste de formulário incompleto executado com sucesso.")
