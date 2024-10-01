from django.shortcuts import render
from .models import CadastrarEquipamento

def index(request):
    return render(request, 'app_produtos/globals/home.html')

def cadastrarEquipamento(request):
    equipamento = {}
    if request.method == 'POST':
        cod_equipamento = request.POST.get('cod_equipamento')    
        nome_equipamento = request.POST.get('nome_equipamento')
        if cod_equipamento and nome_equipamento:
            equipamento = {
                "cod_equipamento": cod_equipamento,
                "nome_equipamento": nome_equipamento
            }
            CadastrarEquipamento.objects.create(**equipamento)

    return render(request, 'app_produtos/globals/cadastrarEquipamento.html', {"equipamento":equipamento})

def editarEquipamento(request):
    return render(request, 'app_produtos/globals/editarEquipamento.html')