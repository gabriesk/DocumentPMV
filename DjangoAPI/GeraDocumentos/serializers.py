from rest_framework import serializers
from GeraDocumentos.models import *

class ItemCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategoria
        fields = "__all__"
    
class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = "__all__"

class ServidoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidores
        fields = "__all__"

class TransferenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencias
        fields = "__all__"
        
class TransferenciasItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferenciasItens
        fields = "__all__"

