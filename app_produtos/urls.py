from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"), 
     path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("cadastrarLogin/", views.cadastrar_login, name="cadastrar_login"),
    path("cadastrarEquipamento/", views.cadastrar_equipamento, name="cadastrar_equipamento"), 
    path("listarEquipamento/", views.listar_equipamento, name="listar_equipamento"),
    path("editarEquipamento/<int:id>", views.editar_equipamento, name="editar_equipamento"),
    path("deletarEquipamento/<int:id>", views.deletar_equipamento, name='deletar_equipamento'), 
    
    path("cadastrarColaborador/", views.cadastrar_colaborador, name="cadastrar_colaborador"),
    path("listarColaborador/", views.listar_colaborador, name="listar_colaborador"),
    path("editarColaborador/<int:id>", views.editar_colaborador, name="editar_colaborador"),
    path("deletarColaborador/<int:id>", views.deletar_colaborador, name='deletar_colaborador'),

    path("relatorioColaborador/", views.relatorio_colaborador, name="relatorio_colaborador"),

    path("registrarAcao/", views.registrar_acao, name="registrar_acao"),

]