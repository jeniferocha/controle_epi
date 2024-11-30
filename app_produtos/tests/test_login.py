import pytest
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_login_com_credenciais_validas(client):
    # Pré-requisitos: Criar um usuário no banco de dados para o teste
    username = "maria"
    password = "123"
    User.objects.create_user(username=username, password=password)

    # Passo 1: Acessar a tela de login (simulado pelo client)
    login_url = reverse('login')  

    # Passo 2 e 3: Inserir nome de usuário e senha válidos
    response = client.post(login_url, {
        'username': username,
        'password': password,
    })

    # Passo 4: Verificar o redirecionamento para a página Home
    assert response.status_code == 302  # Código 302 indica redirecionamento
    assert response.url == reverse('home')  

    # Verificar se a mensagem de sucesso foi adicionada
    response = client.get(reverse('home'))
    messages = list(response.context['messages'])
    assert len(messages) == 1
    assert messages[0].tags == "success"
    assert "Bem-vindo" in messages[0].message, "login não efetuado"

    print(f"Resultado: {messages[0].message}")


@pytest.mark.django_db
def test_login_com_credenciais_invalidas(client):
    # Pré-requisitos: Criar um usuário válido no banco de dados
    username = "maria"
    password = "123"
    User.objects.create_user(username=username, password=password)

    # Acessar a tela de login
    login_url = reverse('login')

    # Inserir nome de usuário e senha inválidos
    response = client.post(login_url, {
        'username': "maria",
        'password': "332211",
    })

    # Verificar que o redirecionamento para 'home' NÃO ocorre
    assert response.status_code == 200  # Deve retornar a página de login novamente
    assert "Usuário ou senha inválidos." in response.content.decode()
