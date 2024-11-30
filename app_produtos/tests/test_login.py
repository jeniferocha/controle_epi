import pytest
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_login_com_credenciais_validas(client):
    
    username = "maria"
    password = "123"
    User.objects.create_user(username=username, password=password)

    
    login_url = reverse('login')  

    
    response = client.post(login_url, {
        'username': username,
        'password': password,
    })

    
    assert response.status_code == 302  
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
    
    username = "maria"
    password = "123"
    User.objects.create_user(username=username, password=password)

    
    login_url = reverse('login')

    # Inserir nome de usuário e senha inválidos
    response = client.post(login_url, {
        'username': "maria",
        'password': "332211",
    })

    # Verificar que o redirecionamento para 'home' NÃO ocorre
    assert response.status_code == 200  
    assert "Usuário ou senha inválidos." in response.content.decode()
