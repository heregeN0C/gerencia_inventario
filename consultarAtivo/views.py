from django.shortcuts import render
from cadEquipamento.models import Equipamento

# Create your views here.
def consultarativo(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'src/consultar_ativo.html', {
        'equipamentos': equipamentos
    })
def consultar_ativo_por_codigo(request, cod_equipamento):
    equipamentos = Equipamento.objects.get(cod_equipamento=cod_equipamento)
    return render(request, 'src/consultar_ativo_por_cod.html', {
        'equipamentos': equipamentos
    })

