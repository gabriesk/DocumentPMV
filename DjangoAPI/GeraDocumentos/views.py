from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from GeraDocumentos.models import *
from GeraDocumentos.serializers import *

# Create your views here.
@csrf_exempt
def ItemCategoriaAPI(request, id=0):
    if request.method=='GET': #READ
        categorias = ItemCategoria.objects.all()
        categorias_serializer = ItemCategoriaSerializer(categorias, many = True)
        return JsonResponse(categorias_serializer.data, safe=False)
    
    elif request.method=='POST': #CREATE
        categorias_data = JSONParser().parse(request)
        categorias_serializer = ItemCategoriaSerializer(data=categorias_data)
        
        if categorias_serializer.is_valid():
            categorias_serializer.save()
            return JsonResponse("Incluido com Sucesso!", safe=False)
        return JsonResponse("Inclusão Falhou.", safe=False)
    
    elif request.method=='PUT': #UPDATE    
        categorias_data = JSONParser().parse(request)
        categorias = ItemCategoria.objects.get(id=categorias_data['id'])
        categorias_serializer = ItemCategoriaSerializer(categorias, data=categorias_data)
        
        if categorias_serializer.is_valid():
            categorias_serializer.save()
            return JsonResponse("Atualizado com Sucesso!", safe=False)
        return JsonResponse("Atualização Falhou.", safe=False)
    
    elif request.method=='DELETE': #DELETE
        categorias = ItemCategoria.objects.get(id=id)
        categorias.delete()
        return JsonResponse("Deletado com Sucesso!", safe=False)

@csrf_exempt
def ItensAPI(request, id=0):
    if request.method=='GET':
        itens = Itens.objects.all()
        itens_serializer = ItensSerializer(itens, many = True)
        return JsonResponse(itens_serializer.data, safe=False)
    
    elif request.method=='POST':
        itens_data = JSONParser().parse(request)
        itens_serializer = ItensSerializer(data=itens_data)
        
        if itens_serializer.is_valid():
            itens_serializer.save()
            return JsonResponse("Incluido com Sucesso!", safe=False)
        return JsonResponse("Inclusão Falhou.", safe=False)
    
    elif request.method=='PUT':   
        itens_data = JSONParser().parse(request)
        itens = Itens.objects.get(id=itens_data['id'])
        itens_serializer = ItensSerializer(itens, data=itens_data)
        
        if itens_serializer.is_valid():
            itens_serializer.save()
            return JsonResponse("Atualizado com Sucesso!", safe=False)
        return JsonResponse("Atualização Falhou.", safe=False)
    
    elif request.method=='DELETE':
        itens = Itens.objects.get(id=id)
        itens.delete()
        return JsonResponse("Deletado com Sucesso!", safe=False)
    
@csrf_exempt
def ServidoresAPI(request, id=0):
    if request.method=='GET':
        servidores = Itens.objects.all()
        servidores_serializer = ServidoresSerializer(servidores, many = True)
        return JsonResponse(servidores_serializer.data, safe=False)
    
    elif request.method=='POST':
        servidores_data = JSONParser().parse(request)
        servidores_serializer = ServidoresSerializer(data=servidores_data)
        
        if servidores_serializer.is_valid():
            servidores_serializer.save()
            return JsonResponse("Incluido com Sucesso!", safe=False)
        return JsonResponse("Inclusão Falhou.", safe=False)
    
    elif request.method=='PUT':   
        servidores_data = JSONParser().parse(request)
        servidores = Itens.objects.get(id=servidores_data['id'])
        servidores_serializer = ServidoresSerializer(servidores, data=servidores_data)
        
        if servidores_serializer.is_valid():
            servidores_serializer.save()
            return JsonResponse("Atualizado com Sucesso!", safe=False)
        return JsonResponse("Atualização Falhou.", safe=False)
    
    elif request.method=='DELETE':
        servidores = Itens.objects.get(id=id)
        servidores.delete()
        return JsonResponse("Deletado com Sucesso!", safe=False)
    
@csrf_exempt
def TransferenciasAPI(request, id=0):
    if request.method=='GET':
        transferencias = Itens.objects.all()
        transferencias_serializer = TransferenciasSerializer(transferencias, many = True)
        return JsonResponse(transferencias_serializer.data, safe=False)
    
    elif request.method=='POST':
        transferencias_data = JSONParser().parse(request)
        transferencias_serializer = TransferenciasSerializer(data=transferencias_data)
        
        if transferencias_serializer.is_valid():
            transferencias_serializer.save()
            return JsonResponse("Incluido com Sucesso!", safe=False)
        return JsonResponse("Inclusão Falhou.", safe=False)
    
    elif request.method=='PUT':   
        transferencias_data = JSONParser().parse(request)
        transferencias = Itens.objects.get(id=transferencias_data['id'])
        transferencias_serializer = TransferenciasSerializer(transferencias, data=transferencias_data)
        
        if transferencias_serializer.is_valid():
            transferencias_serializer.save()
            return JsonResponse("Atualizado com Sucesso!", safe=False)
        return JsonResponse("Atualização Falhou.", safe=False)
    
    elif request.method=='DELETE':
        transferencias = Itens.objects.get(id=id)
        transferencias.delete()
        return JsonResponse("Deletado com Sucesso!", safe=False)
    
@csrf_exempt
def TransferenciasItensAPI(request, id=0):
    if request.method=='GET':
        transferenciasItens = Itens.objects.all()
        transferenciasItens_serializer = TransferenciasItensSerializer(transferenciasItens, many = True)
        return JsonResponse(transferenciasItens_serializer.data, safe=False)
    
    elif request.method=='POST':
        transferenciasItens_data = JSONParser().parse(request)
        transferenciasItens_serializer = TransferenciasItensSerializer(data=transferenciasItens_data)
        
        if transferenciasItens_serializer.is_valid():
            transferenciasItens_serializer.save()
            return JsonResponse("Incluido com Sucesso!", safe=False)
        return JsonResponse("Inclusão Falhou.", safe=False)
    
    elif request.method=='PUT':   
        transferenciasItens_data = JSONParser().parse(request)
        transferenciasItens = Itens.objects.get(id=transferenciasItens_data['id'])
        transferenciasItens_serializer = TransferenciasItensSerializer(transferenciasItens, data=transferenciasItens_data)
        
        if transferenciasItens_serializer.is_valid():
            transferenciasItens_serializer.save()
            return JsonResponse("Atualizado com Sucesso!", safe=False)
        return JsonResponse("Atualização Falhou.", safe=False)
    
    elif request.method=='DELETE':
        transferenciasItens = Itens.objects.get(id=id)
        transferenciasItens.delete()
        return JsonResponse("Deletado com Sucesso!", safe=False)
    