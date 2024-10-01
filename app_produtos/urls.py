from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), 
    path("cadastrarEquipamento/", views.cadastrarEquipamento, name="cadastrarEquipamento"), 
    path("editarEquipamento/", views.editarEquipamento, name="editarEquipamento"),
 
]