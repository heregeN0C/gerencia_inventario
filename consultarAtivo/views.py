from django.shortcuts import render

# Create your views here.
def consultarativo(request):
    return render(request, 'src/consultar_ativo.html')
