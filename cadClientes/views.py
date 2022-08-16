from django.shortcuts import render

# Create your views here.
def cadclientes(request):
    return render(request, 'src/cad_cli.html')