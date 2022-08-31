from django.shortcuts import render, redirect
from .models import FormEquipamento
# Create your views here.
def cadequipamento(request):
    if request.method != 'POST':
        form = FormEquipamento()
        return render(request, 'src/cad_ativo.html', { 'form': form })
    form = FormEquipamento(request.POST)
    if not form.is_valid():
        form = FormEquipamento(request.POST)
        return render(request, 'src/cad_ativo.html', {'form': form})
    form.save()
    return redirect('/')
