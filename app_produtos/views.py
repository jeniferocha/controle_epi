from django.shortcuts import render, redirect
from .models import CadastrarEquipamento, CadastrarColaborador

def index(request):
    return render(request, 'app_produtos/globals/home.html')

def listar_equipamento(request):
    values = CadastrarEquipamento.objects.all()
    cod_equipamento = request.GET.get('cod_equipamento')    
    nome_equipamento = request.GET.get('nome_equipamento')
    if nome_equipamento:
        values = values.filter(nome_equipamento__icontains=nome_equipamento)

    return render(request, 'app_produtos/globals/listarEquipamento.html', {
        "lista_equipamento": values,
        "nome_equipamento": nome_equipamento
    })

def cadastrar_equipamento(request):
    equipamento = {}
    message_type = None
    message_content = None

    if request.method == 'POST':
        cod_equipamento = request.POST.get('cod_equipamento')    
        nome_equipamento = request.POST.get('nome_equipamento')

        if cod_equipamento and nome_equipamento:
            equipamento = {
                "cod_equipamento": cod_equipamento,
                "nome_equipamento": nome_equipamento
            }
            CadastrarEquipamento.objects.create(**equipamento)
            # Mensagem de sucesso
            message_type = 'success'
            message_content = 'Equipamento cadastrado com sucesso!'
        else:
            # Mensagem de erro se os campos não forem preenchidos
            message_type = 'error'
            message_content = 'Equipamento não foi cadastrado. Preencha todos os campos!'

    return render(request, 'app_produtos/globals/cadastrarEquipamento.html', {
        "equipamento": equipamento,
        "message_type": message_type,
        "message_content": message_content
    })

def editar_equipamento(request, id):
    equipamento = CadastrarEquipamento.objects.get(id=id)
    message_type = None
    message_content = None
    
    if request.method == 'POST':
        cod_equipamento = request.POST.get('cod_equipamento')    
        nome_equipamento = request.POST.get('nome_equipamento') 
        
        if cod_equipamento and nome_equipamento:
            equipamento.nome_equipamento = nome_equipamento
            equipamento.cod_equipamento = cod_equipamento
            equipamento.save()    
            return redirect(listar_equipamento)
        else:            
            message_type = 'error'
            message_content = 'Todos os campos são obrigatórios!'    
    
    return render(request, 'app_produtos/globals/editarEquipamento.html', {
        "item": equipamento, 
        "message_type": message_type,
        "message_content": message_content
    })

def deletar_equipamento(request, id):
    equipamento = CadastrarEquipamento.objects.get(id=id)
    equipamento.delete()
    return redirect(listar_equipamento)  


def cadastrar_colaborador(request):
    colaborador = {}
    message_type = None
    message_content = None

    if request.method == 'POST':           
        nome_colaborador = request.POST.get('nome_colaborador')
        cpf = request.POST.get('cpf')
        cargo = request.POST.get('cargo')
        setor = request.POST.get('setor')

        if nome_colaborador and cpf and cargo and setor:
            colaborador = {
                "nome_colaborador": nome_colaborador,
                "cpf": cpf,
                "cargo": cargo,
                "setor": setor
            }
            CadastrarColaborador.objects.create(**colaborador)
            # Mensagem de sucesso
            message_type = 'success'
            message_content = 'Colaborador cadastrado com sucesso!'
        else:
            # Mensagem de erro se os campos não forem preenchidos
            message_type = 'error'
            message_content = 'Colaborador não foi cadastrado. Preencha todos os campos!'        

    return render(request, 'app_produtos/globals/cadastrarEquipamento.html', {
        "colaborador": colaborador,
        "message_type": message_type,
        "message_content": message_content
    })