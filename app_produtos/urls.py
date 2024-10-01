from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), 
    path("cadastrarEquipamento/", views.cadastrar_equipamento, name="cadastrar_equipamento"), 
    path("listarEquipamento/", views.listar_equipamento, name="listar_equipamento"),
    path("editarEquipamento/<int:id>", views.editar_equipamento, name="editar_equipamento"),
    path("deletarEquipamento/<int:id>", views.deletar_equipamento, name='deletar_equipamento'), 

 
]