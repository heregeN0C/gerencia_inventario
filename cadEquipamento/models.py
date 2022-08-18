from django.db import models

# Create your models here.
import cadClientes.models


class Equipamento(models.Model):
    cod_equipamento = models.IntegerField(primary_key=True, serialize=True)
    tipo_equipamento = models.CharField(max_length=50)
    marca_equipamento = models.CharField(max_length=50)
    modelo_equipamento = models.CharField(max_length=100)
    fk_id_cliente = models.ForeignKey(cadClientes.models.Cliente, on_delete=models.CASCADE)
    atendente_equipamento = models.CharField(max_length=100)
    data_chegada = models.DateTimeField('data de chegada')
    solicitacao_equipamento = models.CharField(max_length=250)
