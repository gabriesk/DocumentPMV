from django.db import models

class ItemCategoria(models.Model):
    descricao = models.CharField(max_length=45)

class Itens(models.Model):
    categoria = models.ForeignKey(
        "ItemCategoria", on_delete=models.CASCADE
        )
    pat_sn = models.IntegerField(unique=True)
    modelo = models.CharField(max_length=45)
    fabricante = models.CharField(max_length=45)
    descricao = models.CharField(max_length=256)

class Servidores(models.Model):
    matricula = models.IntegerField(unique=True)
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=45)
    
class Transferencias(models.Model):
    mat_remetente = models.ForeignKey(
        "Servidores", related_name="remetente", on_delete=models.CASCADE
        )
    mat_destinatario = models.ForeignKey(
        "Servidores", related_name="destinatario", on_delete=models.CASCADE
    )
    assinado = models.PositiveSmallIntegerField()
    arquivo_endereco = models.CharField(max_length=250)
    tipo = models.TextField()
    prazo = models.DateField()
    motivo = models.CharField(max_length=256)
    data = models.DateTimeField()

class TransferenciasItens(models.Model):
    id_transferencia = models.ForeignKey(
        "Transferencias", on_delete=models.CASCADE
    )
    id_item = models.ForeignKey(
        "Itens", on_delete=models.CASCADE
    )


# Create your models here.
