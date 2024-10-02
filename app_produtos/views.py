from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import CadastrarEquipamento, CadastrarColaborador, RegistrarAcao

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
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect(reverse('listar_equipamento'))
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
    messages.success(request, 'Equipamento excluído com sucesso!')

    return redirect(reverse('listar_equipamento'))
  


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
            request.session['ultimo_nome'] = nome_colaborador
        else:
            # Mensagem de erro se os campos não forem preenchidos
            message_type = 'error'
            message_content = 'Colaborador não foi cadastrado. Preencha todos os campos!'        

    return render(request, 'app_produtos/globals/cadastrarColaborador.html', {
        "colaborador": colaborador,
        "message_type": message_type,
        "message_content": message_content,
        
    })


def listar_colaborador(request):
    values = CadastrarColaborador.objects.all()
    nome_colaborador = request.GET.get('nome_colaborador')    
    if nome_colaborador:
        values = values.filter(nome_colaborador__icontains=nome_colaborador)

    return render(request, 'app_produtos/globals/listarColaborador.html', {
        "lista_colaborador": values,
        "nome_colaborador": nome_colaborador
    })

def editar_colaborador(request, id):
    colaborador = CadastrarColaborador.objects.get(id=id)
    message_type = None
    message_content = None
    
    if request.method == 'POST':           
        nome_colaborador = request.POST.get('nome_colaborador')
        cpf = request.POST.get('cpf')
        cargo = request.POST.get('cargo')
        setor = request.POST.get('setor')

        if nome_colaborador and cpf and cargo and setor:
            colaborador.nome_colaborador = nome_colaborador
            colaborador.cpf = cpf
            colaborador.cargo = cargo
            colaborador.setor = setor
            colaborador.save()    
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect(reverse('listar_colaborador'))
           
        else:            
            message_type = 'error'
            message_content = 'Todos os campos são obrigatórios!'    
    
    return render(request, 'app_produtos/globals/editarColaborador.html', {
        "item": colaborador, 
        "message_type": message_type,
        "message_content": message_content
    }) 
    
def deletar_colaborador(request, id):   
    colaborador = CadastrarColaborador.objects.get(id=id)
    colaborador.delete()
    messages.success(request, 'Colaborador excluído com sucesso!')
       
    return redirect(reverse('listar_colaborador'))
   
   


def relatorio_colaborador(request):
    values = RegistrarAcao.objects.all()    
    nome_colaborador = request.GET.get('nome_colaborador')    
    if nome_colaborador:
        values = values.filter(colaborador_id__nome_colaborador__icontains=nome_colaborador)

    return render(request, 'app_produtos/globals/relatorioColaborador.html', {
        "registro_acao": values,
        "nome_colaborador": nome_colaborador
    })

   
def registrar_acao(request):
    acao = {}
    message_type = None
    message_content = None

    colaboradores = CadastrarColaborador.objects.all()
    equipamentos = CadastrarEquipamento.objects.all()

    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador_id')    
        equipamento_id = request.POST.get('equipamento_id')
        data_emprestimo = request.POST.get('data_emprestimo')
        data_prevista_devolucao = request.POST.get('data_prevista_devolucao')
        status = request.POST.get('status')
        condicoes = request.POST.get('condicoes')

        if colaborador_id and equipamento_id and data_emprestimo and data_prevista_devolucao and status and condicoes:  
            
            colaborador = CadastrarColaborador.objects.get(id=colaborador_id)
            equipamento = CadastrarEquipamento.objects.get(id=equipamento_id)
            
            acao = {
                "colaborador_id": colaborador,
                "equipamento_id": equipamento,
                "data_emprestimo": data_emprestimo,
                "data_prevista_devolucao": data_prevista_devolucao,
                "status": status,
                "condicoes": condicoes
            }
            RegistrarAcao.objects.create(**acao)
            # Mensagem de sucesso
            message_type = 'success'
            message_content = 'Ação registrada com sucesso!'
            
        else:
            # Mensagem de erro se os campos não forem preenchidos
            message_type = 'error'
            message_content = 'Ação não foi registrada. Preencha todos os campos!'



    return render(request, 'app_produtos/globals/registrarAcao.html', {
        "acao": acao,
        "message_type": message_type,
        "message_content": message_content,
        "colaboradores": colaboradores,
        "equipamentos": equipamentos
    })


def sair(request):
    # Remove o nome do último colaborador da sessão
    del request.session['ultimo_nome']
    # Redireciona para a página inicial ou de login
    return redirect('home')  