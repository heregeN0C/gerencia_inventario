from django.db import models
from django import forms

# Create your models here.
import cadClientes.models




class Equipamento(models.Model):
    cod_equipamento = models.IntegerField(primary_key=True, serialize=True, default=1000)
    tipo_equipamento = models.CharField(max_length=50, default='none', verbose_name='Tipo')
    marca_equipamento = models.CharField(max_length=50, default='none', verbose_name='Marca')
    modelo_equipamento = models.CharField(max_length=100, default='none', verbose_name='Modelo')
    fk_id_cliente = models.ForeignKey(cadClientes.models.Cliente, on_delete=models.CASCADE, default=3654, verbose_name='Cliente')
    atendente_equipamento = models.CharField(max_length=100, default='none', verbose_name='Atendente')
    data_chegada = models.DateTimeField('data de chegada',default='2020/10/10 10:00:00')
    solicitacao_equipamento = models.CharField(max_length=250, default='none', verbose_name='Solicitações exigidas')

class FormEquipamento(forms.ModelForm):
    class Meta:
        model = Equipamento
        exclude = ()
