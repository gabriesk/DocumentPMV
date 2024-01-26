from django.urls import re_path as url
from GeraDocumentos import views

urlpatterns = [
    url(r'^categorias/$', views.ItemCategoriaAPI),
    url(r'^categorias/([0-9]+)$', views.ItemCategoriaAPI),
    
    url(r'^itens/$', views.ItensAPI),
    url(r'^itens/([0-9]+)$', views.ItensAPI),
    
    url(r'^servidores/$', views.ServidoresAPI),
    url(r'^servidores/([0-9]+)$', views.ServidoresAPI),
    
    url(r'^transferencias/$', views.TransferenciasAPI),
    url(r'^transferencias/([0-9]+)$', views.TransferenciasAPI),   

    url(r'^transferenciasitens/$', views.TransferenciasItensAPI),
    url(r'^transferenciasitens/([0-9]+)$', views.TransferenciasItensAPI),   
]

