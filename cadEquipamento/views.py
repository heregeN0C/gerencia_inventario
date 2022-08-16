from django.shortcuts import render

# Create your views here.
def cadequipamento(request):
    return render(request, 'src/cad_ativo.html')