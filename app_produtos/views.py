from django.shortcuts import render, redirect
from .models import CadastrarEquipamento

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



def editar_equipamento(request, id):
    equipamento = CadastrarEquipamento.objects.get(id=id)
    if request.method == 'POST':
        cod_equipamento = request.POST.get('cod_equipamento')    
        nome_equipamento = request.POST.get('nome_equipamento') 
        if cod_equipamento and nome_equipamento:
            equipamento.nome_equipamento = nome_equipamento
            equipamento.cod_equipamento = cod_equipamento
            equipamento.save()
            return redirect(listar_equipamento)  
        else:
            return render(request, 'app_produtos/globals/editarEquipamento.html', {"item":equipamento, "erro":True})
    return render(request, 'app_produtos/globals/editarEquipamento.html', {"item":equipamento})   


def deletar_equipamento(request, id):
    equipamento = CadastrarEquipamento.objects.get(id=id)
    equipamento.delete()
    return redirect(listar_equipamento)  